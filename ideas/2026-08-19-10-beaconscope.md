# BeaconScope

> A tool that generates realistic test data from a database schema in one command.

## Problem
Remote workers struggle to detect their expenses without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Remote workers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Guided onboarding with ready-made templates
- Offline-first with background sync
- Full-text search with smart filters
- Team workspaces with granular permissions
- Responsive dashboard with light and dark mode
- One-click export to CSV and PDF

## Tech Stack
- **Frontend:** Vue 3
- **Backend:** FastAPI (Python)
- **Database:** MongoDB
- **Infra/DevOps:** Fly.io, GitHub Actions CI/CD

## Architecture
A Vue 3 client talks to a FastAPI (Python) API over REST. Data lives in MongoDB. Background jobs handle async work, and the whole stack is containerized and deployed via Fly.io.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
