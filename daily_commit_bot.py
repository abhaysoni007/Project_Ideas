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
from zoneinfo import ZoneInfo
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
        os.environ.setdefault(key, value)


load_dotenv(SCRIPT_DIR / ".env")


def cfg(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


GITHUB_USERNAME = cfg("GITHUB_USERNAME", "abhaysoni007")
GITHUB_REPO = cfg("GITHUB_REPO", "Project_Ideas")
GITHUB_TOKEN = cfg("GITHUB_TOKEN")
GIT_BRANCH = cfg("GIT_BRANCH", "main")
GIT_AUTHOR_NAME = cfg("GIT_AUTHOR_NAME", GITHUB_USERNAME)
GIT_AUTHOR_EMAIL = cfg("GIT_AUTHOR_EMAIL")
WORK_DIR = Path(cfg("WORK_DIR", str(SCRIPT_DIR / "repo_workspace")))

MIN_COMMITS = int(cfg("MIN_COMMITS", "15"))
MAX_COMMITS = int(cfg("MAX_COMMITS", "30"))

WEEKEND_MIN = int(cfg("WEEKEND_MIN", "6"))
WEEKEND_MAX = int(cfg("WEEKEND_MAX", "12"))

# Optional free LLM for real ideas.
# Defaults to Groq.
LLM_API_KEY = cfg("LLM_API_KEY")
LLM_BASE_URL = cfg("LLM_BASE_URL", "https://api.groq.com/openai/v1")
LLM_MODEL = cfg("LLM_MODEL", "llama-3.3-70b-versatile")

# Auto-set to "true" by GitHub Actions.
IN_CI = cfg("GITHUB_ACTIONS") == "true"

REPO_HTTPS = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO}.git"


def authed_remote() -> str:
    """HTTPS remote with token embedded, used only for network ops."""
    if GITHUB_TOKEN:
        return (
            f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}"
            f"@github.com/{GITHUB_USERNAME}/{GITHUB_REPO}.git"
        )
    return REPO_HTTPS


# --------------------------------------------------------------------------- #
# Git helpers
# --------------------------------------------------------------------------- #

import re


_TOKEN_RE = re.compile(
    r"(gh[pousr]_[A-Za-z0-9]+|github_pat_[A-Za-z0-9_]+|"
    r"gsk_[A-Za-z0-9]+|sk-[A-Za-z0-9-]{10,})"
)


def sanitize(text: str) -> str:
    if not text:
        return text

    text = _TOKEN_RE.sub("***TOKEN***", text)

    # Redact credentials embedded in URLs.
    text = re.sub(r"//[^/@\s]+@", "//***@", text)

    for secret in (GITHUB_TOKEN, LLM_API_KEY):
        if secret:
            text = text.replace(secret, "***TOKEN***")

    return text


def run(
    args: list[str],
    cwd: Path | None = None,
    check: bool = True,
) -> str:
    """Run a command and return stdout."""
    print("  $ " + sanitize(" ".join(args)))

    result = subprocess.run(
        args,
        cwd=cwd,
        check=False,
        text=True,
        capture_output=True,
    )

    if result.stdout.strip():
        print(
            "    "
            + sanitize(result.stdout.strip()).replace(
                "\n",
                "\n    ",
            )
        )

    if result.stderr.strip():
        print(
            "    "
            + sanitize(result.stderr.strip()).replace(
                "\n",
                "\n    ",
            ),
            file=sys.stderr,
        )

    if check and result.returncode != 0:
        raise RuntimeError(
            f"Command failed (exit {result.returncode}): "
            f"{sanitize(' '.join(args))}\n"
            f"{sanitize(result.stderr.strip())}"
        )

    return result.stdout.strip()


def ensure_repo() -> Path:
    """Clone the repo if missing, else fetch + reset to latest remote branch."""

    git_dir = WORK_DIR / ".git"

    if not git_dir.exists():
        WORK_DIR.parent.mkdir(parents=True, exist_ok=True)

        print(f"Cloning {REPO_HTTPS} -> {WORK_DIR}")

        run(
            [
                "git",
                "clone",
                authed_remote(),
                str(WORK_DIR),
            ]
        )

        # Remove token from stored origin URL.
        run(
            [
                "git",
                "remote",
                "set-url",
                "origin",
                REPO_HTTPS,
            ],
            cwd=WORK_DIR,
        )

    else:
        print(f"Updating existing clone at {WORK_DIR}")

        run(
            [
                "git",
                "fetch",
                authed_remote(),
                GIT_BRANCH,
            ],
            cwd=WORK_DIR,
            check=False,
        )

        run(
            [
                "git",
                "checkout",
                GIT_BRANCH,
            ],
            cwd=WORK_DIR,
            check=False,
        )

        run(
            [
                "git",
                "reset",
                "--hard",
                f"origin/{GIT_BRANCH}",
            ],
            cwd=WORK_DIR,
            check=False,
        )

    # Per-repository Git identity.
    run(
        [
            "git",
            "config",
            "user.name",
            GIT_AUTHOR_NAME,
        ],
        cwd=WORK_DIR,
    )

    if GIT_AUTHOR_EMAIL:
        run(
            [
                "git",
                "config",
                "user.email",
                GIT_AUTHOR_EMAIL,
            ],
            cwd=WORK_DIR,
        )

    return WORK_DIR


# --------------------------------------------------------------------------- #
# Idea generation
# --------------------------------------------------------------------------- #

DOMAINS = [
    "developer tools",
    "productivity",
    "health & fitness",
    "fintech",
    "education",
    "AI/ML",
    "IoT & hardware",
    "gaming",
    "sustainability",
    "social",
    "e-commerce",
    "data visualization",
    "security",
    "travel",
    "music & audio",
    "accessibility",
    "mental wellness",
    "climate tech",
    "logistics",
    "real estate",
    "agriculture",
    "legal tech",
    "HR & recruiting",
    "creator economy",
    "cybersecurity",
    "robotics",
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

VERBS = [
    "summarize",
    "predict",
    "organize",
    "recommend",
    "track",
    "optimize",
    "detect",
    "personalize",
    "visualize",
    "automate",
    "benchmark",
    "translate",
    "schedule",
    "audit",
    "cluster",
]

THINGS = [
    "daily habits",
    "expenses",
    "code reviews",
    "meeting notes",
    "sensor data",
    "customer feedback",
    "study material",
    "workout plans",
    "news feeds",
    "energy usage",
    "job applications",
    "reading lists",
    "API logs",
    "cloud costs",
    "recipes",
    "travel itineraries",
    "podcast highlights",
    "git commits",
    "screen time",
    "invoices",
]

WHO = [
    "students",
    "small teams",
    "freelancers",
    "developers",
    "remote workers",
    "startups",
    "creators",
    "parents",
    "researchers",
    "gamers",
    "designers",
    "teachers",
    "founders",
    "job seekers",
    "open-source maintainers",
]

# Curated concrete ideas.
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
    """Return count unique ideas."""

    ideas: list[str] = []
    seen: set[str] = set()

    seeds = SEED_IDEAS[:]
    random.shuffle(seeds)

    for idea in seeds[: max(1, count // 2)]:
        if idea not in seen:
            ideas.append(idea)
            seen.add(idea)

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


# --------------------------------------------------------------------------- #
# Full-page project generation
# --------------------------------------------------------------------------- #

NAME_PREFIX = [
    "Snap",
    "Idea",
    "Flow",
    "Nova",
    "Byte",
    "Loop",
    "Pulse",
    "Nest",
    "Vault",
    "Sync",
    "Beacon",
    "Forge",
    "Drift",
    "Echo",
    "Lumen",
    "Quill",
    "Peak",
    "Bolt",
    "Mint",
    "Sage",
    "Orbit",
    "Nimbus",
]

NAME_SUFFIX = [
    "Hub",
    "Kit",
    "Lab",
    "ly",
    "Base",
    "Deck",
    "Pilot",
    "Wise",
    "Craft",
    "Boost",
    "Scope",
    "Mate",
    "Grid",
    "Spark",
    "ify",
    "Path",
    "Bloom",
    "Works",
    "Stack",
    "Desk",
]

FEATURES_POOL = [
    "Email/OAuth sign-in with role-based access control",
    "Responsive dashboard with light and dark mode",
    "Real-time updates over WebSockets",
    "Full-text search with smart filters",
    "One-click export to CSV and PDF",
    "Email and push notifications",
    "Offline-first with background sync",
    "Public REST API with scoped API keys",
    "Usage analytics and an admin panel",
    "Integrations with Slack, Google, and Stripe",
    "AI-assisted recommendations and summaries",
    "Guided onboarding with ready-made templates",
    "Audit log of every change",
    "Team workspaces with granular permissions",
]

WORKLOG_DONE = [
    "Scaffolded the repo and CI pipeline",
    "Designed the database schema and wrote the first migration",
    "Built the authentication flow end to end",
    "Implemented the core API endpoints with validation",
    "Wired up the dashboard layout and routing",
    "Added unit tests for the service layer",
    "Set up Docker Compose for local development",
    "Integrated the third-party payment webhook",
    "Refactored the data-access layer for clarity",
    "Fixed a race condition in the sync worker",
    "Added input validation and error handling",
    "Wrote the README and API documentation",
]

WORKLOG_NEXT = [
    "Add end-to-end tests for the main flow",
    "Set up staging deployment",
    "Implement rate limiting on the public API",
    "Polish the empty and error states in the UI",
    "Add pagination to the list views",
    "Instrument metrics and structured logging",
]


def slugify(text: str) -> str:
    s = re.sub(
        r"[^a-zA-Z0-9]+",
        "-",
        text,
    ).strip("-").lower()

    return s[:40] or "idea"


def _invent_name(used: set) -> str:
    for _ in range(60):
        name = (
            random.choice(NAME_PREFIX)
            + random.choice(NAME_SUFFIX)
        )

        if name.lower() not in used:
            used.add(name.lower())
            return name

    return (
        random.choice(NAME_PREFIX)
        + str(random.randint(10, 999))
    )


def llm_chat(
    prompt: str,
    max_tokens: int = 1200,
    temperature: float = 1.0,
) -> str:
    """One OpenAI-compatible chat call."""

    import json
    import urllib.error
    import urllib.request

    url = LLM_BASE_URL.rstrip("/") + "/chat/completions"

    payload = json.dumps(
        {
            "model": LLM_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": (
                "Mozilla/5.0 "
                "(compatible; daily-commit-bot/1.0)"
            ),
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(
                resp.read().decode("utf-8")
            )

        return data["choices"][0]["message"]["content"].strip()

    except urllib.error.HTTPError as exc:
        body = ""

        try:
            body = exc.read().decode(
                "utf-8",
                "replace",
            )[:300]
        except Exception:
            pass

        raise RuntimeError(
            f"HTTP {exc.code} {exc.reason}: {body}"
        ) from None


# --------------------------------------------------------------------------- #
# Concepts
# --------------------------------------------------------------------------- #

def local_concepts(
    count: int,
) -> list[tuple[str, str]]:
    sentences = generate_ideas_local(count)
    used: set = set()

    return [
        (_invent_name(used), sentence)
        for sentence in sentences
    ]


def generate_concepts(
    count: int,
) -> list[tuple[str, str]]:
    if LLM_API_KEY:
        try:
            prompt = (
                f"Invent {count} original, distinct software or "
                "product startup ideas across different domains. "
                "Output exactly one per line in the format:\n"
                "Name | one-sentence description of what it does "
                "and who it's for\n"
                "No numbering, no markdown, no extra commentary."
            )

            text = llm_chat(
                prompt,
                max_tokens=600,
                temperature=1.15,
            )

            concepts = []
            seen = set()

            for line in text.splitlines():
                line = re.sub(
                    r"^\s*(?:\d+[.)]\s*|[-*•]\s*)",
                    "",
                    line,
                ).strip()

                if "|" in line:
                    name, tag = (
                        p.strip()
                        for p in line.split("|", 1)
                    )

                    name = name.strip("*_# ").strip()

                    if (
                        name
                        and tag
                        and name.lower() not in seen
                    ):
                        seen.add(name.lower())
                        concepts.append((name, tag))

            if concepts:
                print(
                    f"Concepts from LLM: "
                    f"{LLM_MODEL} @ {LLM_BASE_URL}"
                )

                if len(concepts) < count:
                    concepts += local_concepts(
                        count - len(concepts)
                    )

                return concepts[:count]

            print(
                "LLM returned no usable concepts; "
                "using local."
            )

        except Exception as exc:
            print(
                f"LLM concepts failed "
                f"({sanitize(str(exc))}); using local."
            )

    return local_concepts(count)


# --------------------------------------------------------------------------- #
# Full-page idea specifications
# --------------------------------------------------------------------------- #

def local_page(
    name: str,
    tagline: str,
) -> str:
    features = random.sample(
        FEATURES_POOL,
        6,
    )

    front = random.choice(
        [
            "React",
            "Next.js",
            "Vue 3",
            "SvelteKit",
            "React Native",
            "Flutter",
        ]
    )

    back = random.choice(
        [
            "Node.js + Express",
            "FastAPI (Python)",
            "Django",
            "Go (Gin)",
            "NestJS",
        ]
    )

    db = random.choice(
        [
            "PostgreSQL",
            "MongoDB",
            "SQLite",
            "MySQL",
            "Supabase",
        ]
    )

    infra = random.choice(
        [
            "Docker + AWS ECS",
            "Vercel",
            "Fly.io",
            "Railway",
            "GCP Cloud Run",
        ]
    )

    who = random.choice(WHO)

    feat_md = "\n".join(
        f"- {feature}"
        for feature in features
    )

    return (
        f"# {name}\n\n"
        f"> {tagline}\n\n"
        f"## Problem\n"
        f"{who.capitalize()} struggle to "
        f"{random.choice(VERBS)} their "
        f"{random.choice(THINGS)} without switching "
        "between too many disconnected tools. "
        "Existing options are either too generic or "
        "too expensive for their needs.\n\n"
        f"## Target Users\n"
        f"- {who.capitalize()}\n"
        "- Small teams and startups\n"
        "- Anyone who needs a focused, no-friction tool\n\n"
        f"## Key Features\n"
        f"{feat_md}\n\n"
        f"## Tech Stack\n"
        f"- **Frontend:** {front}\n"
        f"- **Backend:** {back}\n"
        f"- **Database:** {db}\n"
        f"- **Infra/DevOps:** {infra}, "
        "GitHub Actions CI/CD\n\n"
        f"## Architecture\n"
        f"A {front} client talks to a {back} API over REST. "
        f"Data lives in {db}. Background jobs handle async "
        f"work, and the whole stack is containerized and "
        f"deployed via {infra}.\n\n"
        f"## Roadmap\n"
        "- **v1** — Core flow, auth, and the dashboard\n"
        "- **v2** — Integrations, notifications, and "
        "the public API\n"
        "- **v3** — Team features, analytics, and "
        "mobile support\n"
    )


def generate_page(
    name: str,
    tagline: str,
) -> str:
    if LLM_API_KEY:
        try:
            prompt = (
                "Write a detailed one-page project specification "
                "in GitHub-Flavored Markdown for a software product.\n"
                f"Product name: {name}\n"
                f"Concept: {tagline}\n\n"
                "Use exactly these sections and headings, "
                "in this order:\n"
                f"# {name}\n"
                "> a punchy one-line tagline\n"
                "## Problem (2-3 sentences)\n"
                "## Target Users (bulleted)\n"
                "## Key Features (5-7 bullets)\n"
                "## Tech Stack (bullets grouped as Frontend, "
                "Backend, Database, Infra/DevOps, and AI/ML "
                "if relevant)\n"
                "## Architecture (a short paragraph)\n"
                "## Roadmap (v1, v2, v3 bullets)\n\n"
                "Be concrete and realistic with specific "
                "technology choices. Output only the markdown, "
                "nothing else."
            )

            md = llm_chat(
                prompt,
                max_tokens=1600,
                temperature=0.9,
            )

            if len(md) > 200:
                return (
                    md
                    if md.lstrip().startswith("#")
                    else f"# {name}\n\n{md}"
                )

            print(
                f"LLM page too short for {name}; "
                "using local."
            )

        except Exception as exc:
            print(
                f"LLM page failed "
                f"({sanitize(str(exc))}); using local."
            )

    return local_page(name, tagline)


# --------------------------------------------------------------------------- #
# Daily work log
# --------------------------------------------------------------------------- #

def local_work_log(
    concepts: list,
    today: str,
) -> str:
    done = random.sample(
        WORKLOG_DONE,
        5,
    )

    nxt = random.sample(
        WORKLOG_NEXT,
        3,
    )

    projects = "\n".join(
        f"- **{n}** — {t}"
        for n, t in concepts
    )

    done_md = "\n".join(
        f"- {d}"
        for d in done
    )

    next_md = "\n".join(
        f"- {x}"
        for x in nxt
    )

    return (
        f"# Daily Work Log — {today}\n\n"
        f"## Projects touched today\n"
        f"{projects}\n\n"
        f"## Done today\n"
        f"{done_md}\n\n"
        "## In progress\n"
        "- Iterating on the core feature set based on "
        "early feedback\n"
        "- Cleaning up the API surface before freezing v1\n\n"
        "## Blockers\n"
        "- None right now\n\n"
        f"## Next up\n"
        f"{next_md}\n"
    )


def generate_work_log(
    concepts: list,
    today: str,
) -> str:
    names = ", ".join(
        n
        for n, _ in concepts
    )

    if LLM_API_KEY:
        try:
            prompt = (
                "Write a concise daily developer work log "
                f"in GitHub Markdown for {today}.\n"
                "Frame it as realistic progress across these "
                f"side projects: {names}.\n"
                "Use this structure:\n"
                f"# Daily Work Log — {today}\n"
                "## Done today (4-6 concrete dev tasks as bullets)\n"
                "## In progress (1-2 bullets)\n"
                "## Blockers (0-1 bullet)\n"
                "## Next up (2-3 bullets)\n"
                "Write it like a real developer's standup notes. "
                "Output only markdown."
            )

            md = llm_chat(
                prompt,
                max_tokens=700,
                temperature=0.9,
            )

            if len(md) > 100:
                return (
                    md
                    if md.lstrip().startswith("#")
                    else f"# Daily Work Log — {today}\n\n{md}"
                )

        except Exception as exc:
            print(
                f"LLM work-log failed "
                f"({sanitize(str(exc))}); using local."
            )

    return local_work_log(
        concepts,
        today,
    )


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main() -> int:
    if not GIT_AUTHOR_EMAIL:
        print(
            "WARNING: GIT_AUTHOR_EMAIL not set. "
            "Commits may not count toward your contribution "
            "graph unless the email is verified on your GitHub account."
        )

    if IN_CI:
        # GitHub Actions already checked out the repo.
        repo = Path(
            cfg(
                "GITHUB_WORKSPACE",
                str(SCRIPT_DIR),
            )
        )

        print(
            f"Running in GitHub Actions; "
            f"using checked-out repo at {repo}"
        )

        run(
            [
                "git",
                "config",
                "user.name",
                GIT_AUTHOR_NAME,
            ],
            cwd=repo,
        )

        if GIT_AUTHOR_EMAIL:
            run(
                [
                    "git",
                    "config",
                    "user.email",
                    GIT_AUTHOR_EMAIL,
                ],
                cwd=repo,
            )

    else:
        if not GITHUB_TOKEN:
            print(
                "ERROR: GITHUB_TOKEN not set. "
                "Create a PAT with 'repo' scope and put it in .env."
            )
            return 1

        repo = ensure_repo()

    ideas_dir = repo / "ideas"
    ideas_dir.mkdir(exist_ok=True)

    work_dir = repo / "daily-work"
    work_dir.mkdir(exist_ok=True)

    # ----------------------------------------------------------------------- #
    # IMPORTANT:
    # GitHub Actions runners use UTC by default.
    # Use India Standard Time so the bot's calendar day matches India.
    # ----------------------------------------------------------------------- #

    now = datetime.now(
        ZoneInfo("Asia/Kolkata")
    )

    is_weekend = now.weekday() >= 5

    if is_weekend:
        n_ideas = random.randint(
            WEEKEND_MIN,
            WEEKEND_MAX,
        )
    else:
        n_ideas = random.randint(
            MIN_COMMITS,
            MAX_COMMITS,
        )

    today = now.strftime("%Y-%m-%d")

    print(
        f"{'Weekend' if is_weekend else 'Weekday'} "
        f"run -> {n_ideas} idea commits"
    )

    # ----------------------------------------------------------------------- #
    # Commit helper
    # ----------------------------------------------------------------------- #

    def commit(
        path: Path,
        message: str,
    ) -> None:

        run(
            [
                "git",
                "add",
                str(path.relative_to(repo)),
            ],
            cwd=repo,
        )

        env = os.environ.copy()

        if GIT_AUTHOR_EMAIL:
            env["GIT_AUTHOR_EMAIL"] = GIT_AUTHOR_EMAIL
            env["GIT_COMMITTER_EMAIL"] = GIT_AUTHOR_EMAIL
            env["GIT_AUTHOR_NAME"] = GIT_AUTHOR_NAME
            env["GIT_COMMITTER_NAME"] = GIT_AUTHOR_NAME

        # ------------------------------------------------------------------- #
        # IMPORTANT:
        # Store Git's author and committer timestamps in IST.
        #
        # This fixes the issue where a 1:00 AM IST commit was stored as
        # 19:30 UTC from the previous calendar day.
        # ------------------------------------------------------------------- #

        commit_time = now.isoformat()

        env["GIT_AUTHOR_DATE"] = commit_time
        env["GIT_COMMITTER_DATE"] = commit_time

        subprocess.run(
            [
                "git",
                "commit",
                "-m",
                message,
            ],
            cwd=repo,
            check=True,
            text=True,
            env=env,
        )

    # ----------------------------------------------------------------------- #
    # Generate ideas
    # ----------------------------------------------------------------------- #

    print(
        f"\nGenerating {n_ideas} full idea pages for {today}..."
    )

    concepts = generate_concepts(
        n_ideas
    )

    for i, (name, tagline) in enumerate(
        concepts,
        start=1,
    ):
        page = generate_page(
            name,
            tagline,
        )

        base = (
            f"{today}-{i:02d}-"
            f"{slugify(name)}"
        )

        fname = ideas_dir / f"{base}.md"

        k = 1

        while fname.exists():
            k += 1
            fname = ideas_dir / f"{base}-{k}.md"

        fname.write_text(
            page.rstrip() + "\n",
            encoding="utf-8",
        )

        commit(
            fname,
            f"Add idea: {name} - {tagline[:60]}",
        )

        print(
            f"  committed idea "
            f"[{i}/{n_ideas}] {fname.name}"
        )

    # ----------------------------------------------------------------------- #
    # Daily developer work log
    # ----------------------------------------------------------------------- #

    print(
        "Generating daily work log..."
    )

    wlog = generate_work_log(
        concepts,
        today,
    )

    wname = work_dir / f"{today}.md"

    k = 1

    while wname.exists():
        k += 1
        wname = work_dir / f"{today}-{k}.md"

    wname.write_text(
        wlog.rstrip() + "\n",
        encoding="utf-8",
    )

    commit(
        wname,
        f"Daily work log for {today}",
    )

    print(
        f"  committed work log {wname.name}"
    )

    # ----------------------------------------------------------------------- #
    # Push
    # ----------------------------------------------------------------------- #

    total = n_ideas + 1

    print(
        "\nPushing to GitHub..."
    )

    if IN_CI:
        # Push using credentials configured by actions/checkout.
        run(
            [
                "git",
                "push",
                "origin",
                f"HEAD:{GIT_BRANCH}",
            ],
            cwd=repo,
        )

    else:
        run(
            [
                "git",
                "push",
                authed_remote(),
                f"HEAD:{GIT_BRANCH}",
            ],
            cwd=repo,
        )

    print(
        f"\nDone. Pushed {total} commits "
        f"to {GITHUB_USERNAME}/{GITHUB_REPO}."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
