#!/usr/bin/env python3
"""
Daily AI commit bot.

Every run it:
  1. Clones/pulls your GitHub repo into a local work folder.
  2. Generates 5-6 project ideas (via Claude API if a key is set, else a local
     idea generator).
  3. Writes each idea to ideas/YYYY-MM-DD-<n>.md and makes ONE commit per idea.
  4. Pushes everything back to GitHub.

Contributions count toward your graph only when the commit author email is a
verified email on your GitHub account, so set GIT_AUTHOR_EMAIL accordingly.

Configure via environment variables or a .env file next to this script.
See config.example.env.
"""

from __future__ import annotations

import os
import random
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# --------------------------------------------------------------------------- #
# Config loading (.env is optional; plain env vars work too)
# --------------------------------------------------------------------------- #

SCRIPT_DIR = Path(__file__).resolve().parent


def load_dotenv(path: Path) -> None:
    """Minimal .env loader so python-dotenv is not a hard dependency."""
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        # Do not overwrite a value already present in the real environment.
        os.environ.setdefault(key, value)


load_dotenv(SCRIPT_DIR / ".env")


def cfg(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


GITHUB_USERNAME = cfg("GITHUB_USERNAME", "abhaysoni007")
GITHUB_REPO = cfg("GITHUB_REPO", "Project_Ideas")
GITHUB_TOKEN = cfg("GITHUB_TOKEN")  # personal access token with 'repo' scope
GIT_BRANCH = cfg("GIT_BRANCH", "main")
GIT_AUTHOR_NAME = cfg("GIT_AUTHOR_NAME", GITHUB_USERNAME)
GIT_AUTHOR_EMAIL = cfg("GIT_AUTHOR_EMAIL")  # MUST be verified on your GitHub account
WORK_DIR = Path(cfg("WORK_DIR", str(SCRIPT_DIR / "repo_workspace")))
MIN_COMMITS = int(cfg("MIN_COMMITS", "5"))
MAX_COMMITS = int(cfg("MAX_COMMITS", "6"))

# Optional free LLM for real ideas. Defaults target Groq (free, no credit card).
# Leave LLM_API_KEY empty to use the built-in local generator instead.
# Works with any OpenAI-compatible API (Groq, OpenRouter, Together, etc.).
LLM_API_KEY = cfg("LLM_API_KEY")
LLM_BASE_URL = cfg("LLM_BASE_URL", "https://api.groq.com/openai/v1")
LLM_MODEL = cfg("LLM_MODEL", "llama-3.3-70b-versatile")

# Auto-set to "true" by GitHub Actions. In CI we operate on the already
# checked-out repo instead of cloning, and push via the checkout credentials.
IN_CI = cfg("GITHUB_ACTIONS") == "true"

REPO_HTTPS = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO}.git"


def authed_remote() -> str:
    """HTTPS remote with token embedded, used only for network ops (never stored)."""
    if GITHUB_TOKEN:
        return f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{GITHUB_REPO}.git"
    return REPO_HTTPS


# --------------------------------------------------------------------------- #
# Git helpers
# --------------------------------------------------------------------------- #


import re

# Redacts anything that looks like a token so it can never reach logs/tracebacks.
_TOKEN_RE = re.compile(
    r"(gh[pousr]_[A-Za-z0-9]+|github_pat_[A-Za-z0-9_]+|gsk_[A-Za-z0-9]+|sk-[A-Za-z0-9-]{10,})"
)


def sanitize(text: str) -> str:
    if not text:
        return text
    text = _TOKEN_RE.sub("***TOKEN***", text)
    # Redact credentials embedded in any URL: https://user:pass@host -> https://***@host
    text = re.sub(r"//[^/@\s]+@", "//***@", text)
    for secret in (GITHUB_TOKEN, LLM_API_KEY):
        if secret:
            text = text.replace(secret, "***TOKEN***")
    return text


def run(args: list[str], cwd: Path | None = None, check: bool = True) -> str:
    """Run a command, return stdout. Tokens are scrubbed from all output and errors."""
    print("  $ " + sanitize(" ".join(args)))
    # check=False here: we handle failures ourselves so raw args (with token)
    # never surface in a CalledProcessError traceback.
    result = subprocess.run(args, cwd=cwd, check=False, text=True, capture_output=True)
    if result.stdout.strip():
        print("    " + sanitize(result.stdout.strip()).replace("\n", "\n    "))
    if result.stderr.strip():
        print("    " + sanitize(result.stderr.strip()).replace("\n", "\n    "), file=sys.stderr)
    if check and result.returncode != 0:
        raise RuntimeError(
            f"Command failed (exit {result.returncode}): {sanitize(' '.join(args))}\n"
            f"{sanitize(result.stderr.strip())}"
        )
    return result.stdout.strip()


def ensure_repo() -> Path:
    """Clone the repo if missing, else fetch + reset to latest remote branch."""
    git_dir = WORK_DIR / ".git"
    if not git_dir.exists():
        WORK_DIR.parent.mkdir(parents=True, exist_ok=True)
        print(f"Cloning {REPO_HTTPS} -> {WORK_DIR}")
        run(["git", "clone", authed_remote(), str(WORK_DIR)])
        # git clone stores the URL (with token) as origin — scrub it back to plain.
        run(["git", "remote", "set-url", "origin", REPO_HTTPS], cwd=WORK_DIR)
    else:
        print(f"Updating existing clone at {WORK_DIR}")
        # check=False: an empty remote has no branch yet — that's fine.
        run(["git", "fetch", authed_remote(), GIT_BRANCH], cwd=WORK_DIR, check=False)
        # Align local branch with remote; discards any leftover local mess.
        run(["git", "checkout", GIT_BRANCH], cwd=WORK_DIR, check=False)
        run(["git", "reset", "--hard", f"origin/{GIT_BRANCH}"], cwd=WORK_DIR, check=False)

    # Per-repo identity for commits (does not touch global git config).
    run(["git", "config", "user.name", GIT_AUTHOR_NAME], cwd=WORK_DIR)
    if GIT_AUTHOR_EMAIL:
        run(["git", "config", "user.email", GIT_AUTHOR_EMAIL], cwd=WORK_DIR)
    return WORK_DIR


# --------------------------------------------------------------------------- #
# Idea generation
# --------------------------------------------------------------------------- #

DOMAINS = [
    "developer tools", "productivity", "health & fitness", "fintech", "education",
    "AI/ML", "IoT & hardware", "gaming", "sustainability", "social", "e-commerce",
    "data visualization", "security", "travel", "music & audio", "accessibility",
    "mental wellness", "climate tech", "logistics", "real estate", "agriculture",
    "legal tech", "HR & recruiting", "creator economy", "cybersecurity", "robotics",
]
PATTERNS = [
    "A {domain} app that uses AI to {verb} {thing} for {who}.",
    "A CLI tool that automates {thing} in {domain} workflows.",
    "A browser extension that helps {who} {verb} {thing} while they browse.",
    "A dashboard that turns raw {thing} into actionable {domain} insights.",
    "A mobile app that gamifies {thing} to keep {who} engaged.",
    "An API service that lets developers add {thing} to any {domain} product.",
    "A Slack/Discord bot that helps {who} {verb} {thing} without leaving chat.",
    "A self-hosted tool that lets {who} {verb} {thing} with full data privacy.",
    "A no-code builder for {who} to {verb} {thing} without writing code.",
    "A VS Code extension that helps {who} {verb} {thing} inside the editor.",
    "A weekly-digest service that {verb}s {thing} and emails {who} a summary.",
    "A Chrome-to-mobile sync app that lets {who} {verb} {thing} across devices.",
]
VERBS = ["summarize", "predict", "organize", "recommend", "track", "optimize",
         "detect", "personalize", "visualize", "automate", "benchmark", "translate",
         "schedule", "audit", "cluster"]
THINGS = ["daily habits", "expenses", "code reviews", "meeting notes", "sensor data",
          "customer feedback", "study material", "workout plans", "news feeds",
          "energy usage", "job applications", "reading lists", "API logs",
          "cloud costs", "recipes", "travel itineraries", "podcast highlights",
          "git commits", "screen time", "invoices"]
WHO = ["students", "small teams", "freelancers", "developers", "remote workers",
       "startups", "creators", "parents", "researchers", "gamers", "designers",
       "teachers", "founders", "job seekers", "open-source maintainers"]

# Curated concrete ideas — mixed in so output isn't only templated combinations.
SEED_IDEAS = [
    "A tool that scans your GitHub repos and auto-generates a portfolio site from your top projects.",
    "An app that converts long YouTube tutorials into step-by-step markdown notes.",
    "A CLI that detects unused dependencies across a monorepo and opens cleanup PRs.",
    "A browser extension that shows the carbon footprint of each website you visit.",
    "A habit tracker that pairs you with an accountability buddy who has the same goal.",
    "A service that turns your bank statements into a plain-English monthly spending story.",
    "An AI-free rule-based linter for accessibility issues in HTML emails.",
    "A tool that watches competitor pricing pages and alerts you when prices change.",
    "A local-first note app where every note is a git commit you can diff over time.",
    "A dashboard that grades your resume against a job description and lists gaps.",
    "A Pomodoro timer that mutes Slack and sets your calendar to busy automatically.",
    "A tool that generates realistic test data from a database schema in one command.",
    "An app that suggests recipes based on what's about to expire in your fridge.",
    "A extension that summarizes long GitHub issues and their comment threads.",
    "A self-hosted read-later app that strips ads and estimates reading time.",
    "A tool that maps your codebase into an interactive dependency graph.",
    "A budgeting app for freelancers that sets aside tax money on every invoice paid.",
    "A CLI that turns terminal session recordings into shareable animated SVGs.",
    "A study app that turns your highlighted PDFs into spaced-repetition flashcards.",
    "A tool that audits a website's Core Web Vitals and suggests concrete fixes.",
]


def generate_ideas_local(count: int) -> list[str]:
    """Return `count` unique ideas: some curated, the rest templated."""
    ideas: list[str] = []
    seen: set[str] = set()

    # Pull a few curated ideas first for variety.
    seeds = SEED_IDEAS[:]
    random.shuffle(seeds)
    for idea in seeds[: max(1, count // 2)]:
        if idea not in seen:
            ideas.append(idea)
            seen.add(idea)

    # Fill the rest with templated combinations, avoiding duplicates.
    attempts = 0
    while len(ideas) < count and attempts < count * 50:
        attempts += 1
        idea = random.choice(PATTERNS).format(
            domain=random.choice(DOMAINS),
            verb=random.choice(VERBS),
            thing=random.choice(THINGS),
            who=random.choice(WHO),
        )
        if idea not in seen:
            ideas.append(idea)
            seen.add(idea)

    random.shuffle(ideas)
    return ideas[:count]


def generate_ideas_llm(count: int) -> list[str]:
    """Call an OpenAI-compatible chat API (Groq by default — free) for ideas.
    Uses only the standard library. Falls back to local on any failure."""
    import json
    import urllib.request

    url = LLM_BASE_URL.rstrip("/") + "/chat/completions"
    prompt = (
        f"Give me {count} concrete, original software or product project ideas. "
        "One idea per line. No numbering, no bullets, no preamble, no markdown. "
        "Each idea must be a single sentence describing what it does and who it's for."
    )
    payload = json.dumps({
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 800,
        "temperature": 1.0,
    }).encode("utf-8")
    req = urllib.request.Request(
        url, data=payload, method="POST",
        headers={
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        text = data["choices"][0]["message"]["content"]
        ideas = []
        for line in text.splitlines():
            # Strip leading list markers like "1. ", "- ", "* ".
            line = re.sub(r"^\s*(?:\d+[.)]\s*|[-*•]\s*)", "", line).strip()
            if len(line) > 12:
                ideas.append(line)
        if len(ideas) < count:
            ideas += generate_ideas_local(count - len(ideas))
        print(f"Ideas from LLM: {LLM_MODEL} @ {LLM_BASE_URL}")
        return ideas[:count]
    except Exception as exc:  # network / auth / quota / bad model — degrade gracefully
        print(f"LLM generation failed ({sanitize(str(exc))}); using local generator.")
        return generate_ideas_local(count)


def generate_ideas(count: int) -> list[str]:
    if LLM_API_KEY:
        return generate_ideas_llm(count)
    return generate_ideas_local(count)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def main() -> int:
    if not GIT_AUTHOR_EMAIL:
        print("WARNING: GIT_AUTHOR_EMAIL not set. Commits may not count toward your "
              "contribution graph unless the email is verified on your GitHub account.")

    if IN_CI:
        # GitHub Actions already checked out the repo; work in it directly.
        repo = Path(cfg("GITHUB_WORKSPACE", str(SCRIPT_DIR)))
        print(f"Running in GitHub Actions; using checked-out repo at {repo}")
        run(["git", "config", "user.name", GIT_AUTHOR_NAME], cwd=repo)
        if GIT_AUTHOR_EMAIL:
            run(["git", "config", "user.email", GIT_AUTHOR_EMAIL], cwd=repo)
    else:
        if not GITHUB_TOKEN:
            print("ERROR: GITHUB_TOKEN not set. Create a PAT with 'repo' scope and put it in .env.")
            return 1
        repo = ensure_repo()

    ideas_dir = repo / "ideas"
    ideas_dir.mkdir(exist_ok=True)

    n_commits = random.randint(MIN_COMMITS, MAX_COMMITS)
    today = datetime.now().strftime("%Y-%m-%d")
    stamp = datetime.now().strftime("%H:%M:%S")
    print(f"\nGenerating {n_commits} ideas for {today}...")
    ideas = generate_ideas(n_commits)

    for i, idea in enumerate(ideas, start=1):
        # Unique filename per commit so each is a real, distinct change.
        fname = ideas_dir / f"{today}-{i:02d}.md"
        suffix = 1
        while fname.exists():
            suffix += 1
            fname = ideas_dir / f"{today}-{i:02d}-{suffix}.md"

        content = (
            f"# Project Idea\n\n"
            f"- **Date:** {today} {stamp}\n"
            f"- **#{i} of {n_commits} today**\n\n"
            f"{idea}\n"
        )
        fname.write_text(content, encoding="utf-8")

        run(["git", "add", str(fname.relative_to(repo))], cwd=repo)
        commit_msg = f"Add project idea: {idea[:60]}"
        env = os.environ.copy()
        if GIT_AUTHOR_EMAIL:
            env["GIT_AUTHOR_EMAIL"] = GIT_AUTHOR_EMAIL
            env["GIT_COMMITTER_EMAIL"] = GIT_AUTHOR_EMAIL
            env["GIT_AUTHOR_NAME"] = GIT_AUTHOR_NAME
            env["GIT_COMMITTER_NAME"] = GIT_AUTHOR_NAME
        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=repo, check=True, text=True, env=env,
        )
        print(f"  committed [{i}/{n_commits}] {fname.name}")

    print("\nPushing to GitHub...")
    if IN_CI:
        # Push using credentials configured by actions/checkout (no token in URL).
        run(["git", "push", "origin", f"HEAD:{GIT_BRANCH}"], cwd=repo)
    else:
        run(["git", "push", authed_remote(), f"HEAD:{GIT_BRANCH}"], cwd=repo)
    print(f"\nDone. Pushed {n_commits} commits to {GITHUB_USERNAME}/{GITHUB_REPO}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
