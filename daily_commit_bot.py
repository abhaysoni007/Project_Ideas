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
ANTHROPIC_API_KEY = cfg("ANTHROPIC_API_KEY")
ANTHROPIC_MODEL = cfg("ANTHROPIC_MODEL", "claude-sonnet-5")

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
_TOKEN_RE = re.compile(r"(gh[pousr]_[A-Za-z0-9]+|github_pat_[A-Za-z0-9_]+)")


def sanitize(text: str) -> str:
    if not text:
        return text
    text = _TOKEN_RE.sub("***TOKEN***", text)
    # Redact credentials embedded in any URL: https://user:pass@host -> https://***@host
    text = re.sub(r"//[^/@\s]+@", "//***@", text)
    if GITHUB_TOKEN:
        text = text.replace(GITHUB_TOKEN, "***TOKEN***")
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
]
PATTERNS = [
    "A {domain} app that uses AI to {verb} {thing} for {who}.",
    "A CLI tool that automates {thing} in {domain} workflows.",
    "A browser extension that helps {who} {verb} {thing} while they browse.",
    "A dashboard that turns raw {thing} into actionable {domain} insights.",
    "A mobile app that gamifies {thing} to keep {who} engaged.",
    "An API service that lets developers add {thing} to any {domain} product.",
]
VERBS = ["summarize", "predict", "organize", "recommend", "track", "optimize", "detect", "personalize"]
THINGS = ["daily habits", "expenses", "code reviews", "meeting notes", "sensor data",
          "customer feedback", "study material", "workout plans", "news feeds", "energy usage"]
WHO = ["students", "small teams", "freelancers", "developers", "remote workers",
       "startups", "creators", "parents", "researchers", "gamers"]


def generate_ideas_local(count: int) -> list[str]:
    ideas = []
    for _ in range(count):
        pattern = random.choice(PATTERNS)
        ideas.append(pattern.format(
            domain=random.choice(DOMAINS),
            verb=random.choice(VERBS),
            thing=random.choice(THINGS),
            who=random.choice(WHO),
        ))
    return ideas


def generate_ideas_ai(count: int) -> list[str]:
    """Use Claude to generate ideas. Falls back to local on any failure."""
    try:
        from anthropic import Anthropic
    except ImportError:
        print("anthropic package not installed; using local generator.")
        return generate_ideas_local(count)

    try:
        client = Anthropic(api_key=ANTHROPIC_API_KEY)
        prompt = (
            f"Give me {count} concrete, original software/product project ideas. "
            "One per line, no numbering, no preamble. Each idea should be a single "
            "sentence describing what it does and who it's for."
        )
        msg = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        text = "".join(block.text for block in msg.content if getattr(block, "type", "") == "text")
        ideas = [line.strip(" -•\t") for line in text.splitlines() if line.strip()]
        ideas = [i for i in ideas if len(i) > 10]
        if len(ideas) < count:
            ideas += generate_ideas_local(count - len(ideas))
        return ideas[:count]
    except Exception as exc:  # network / auth / quota — degrade gracefully
        print(f"AI generation failed ({exc}); using local generator.")
        return generate_ideas_local(count)


def generate_ideas(count: int) -> list[str]:
    if ANTHROPIC_API_KEY:
        return generate_ideas_ai(count)
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
