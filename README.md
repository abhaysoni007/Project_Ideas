# Daily AI Commit Bot

Pushes **5–6 commits every day at 10 AM** to `github.com/abhaysoni007/Project_Ideas`.
Each commit adds a real project-idea file (`ideas/YYYY-MM-DD-NN.md`) — meaningful
content, not empty commits. Ideas come from Claude if you set an API key, otherwise
from a built-in generator (no cost).

## Contribution graph note

Commits count toward your green squares only when the **commit author email is a
verified email on your GitHub account**. Set `GIT_AUTHOR_EMAIL` to that email.

---

## 1. Setup

```powershell
cd "c:\Users\yuvra\Downloads\OppoEnco2\ai automation"
copy config.example.env .env
notepad .env        # fill in GITHUB_TOKEN and GIT_AUTHOR_EMAIL
pip install -r requirements.txt   # optional, only for AI-generated ideas
```

**Get a token:** https://github.com/settings/tokens → generate a token with the
`repo` scope → paste it as `GITHUB_TOKEN` in `.env`.

## 2. Test it once

```powershell
py daily_commit_bot.py
```

This clones the repo into `repo_workspace/`, makes 5–6 commits, and pushes.
Check your repo — you should see new files under `ideas/`.

## 3. Schedule it for 10 AM daily

### Option A — Windows Task Scheduler (runs on your PC)

```powershell
powershell -ExecutionPolicy Bypass -File .\setup_task_scheduler.ps1
```

Runs daily at 10:00 AM. If the PC was off/asleep, it runs as soon as it's back on.
Test the scheduled task immediately:

```powershell
Start-ScheduledTask -TaskName DailyGithubCommitBot
```

Remove it later:

```powershell
Unregister-ScheduledTask -TaskName DailyGithubCommitBot -Confirm:$false
```

### Option B — GitHub Actions (cloud, PC can be off)

1. Push the `.github/workflows/daily-commits.yml` file to your repo.
2. In the repo: **Settings → Secrets and variables → Actions** add:
   - `PAT_TOKEN` — a personal access token with `repo` scope
   - `GIT_EMAIL` — your GitHub-verified email
   - `ANTHROPIC_API_KEY` — optional
3. Runs daily at **04:30 UTC = 10:00 AM IST**. Trigger manually anytime from the
   **Actions** tab (Run workflow).

> Actions is the better choice if your PC isn't always on at 10 AM.

---

## Config reference

| Variable | Meaning | Default |
|---|---|---|
| `GITHUB_TOKEN` | PAT with `repo` scope (required) | — |
| `GIT_AUTHOR_EMAIL` | Verified GitHub email (required for graph) | — |
| `GITHUB_USERNAME` | Your username | `abhaysoni007` |
| `GITHUB_REPO` | Target repo | `Project_Ideas` |
| `GIT_BRANCH` | Branch to push | `main` |
| `MIN_COMMITS` / `MAX_COMMITS` | Commits per day (random range) | `5` / `6` |
| `ANTHROPIC_API_KEY` | Enables real AI ideas | empty → local generator |
| `WORK_DIR` | Local clone path | `./repo_workspace` |

## Notes

- The token is used only for network calls and is **never** written to `.git/config`.
- `.env` and `repo_workspace/` are git-ignored — don't commit your token.
- Auto-committing inflates your contribution graph; keeping the content real
  (actual idea logs) keeps it honest.
