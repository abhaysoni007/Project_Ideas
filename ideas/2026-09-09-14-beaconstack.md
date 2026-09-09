# BeaconStack

> A budgeting app for freelancers that sets aside tax money on every invoice paid.

## Problem
Parents struggle to translate their news feeds without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Parents
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email and push notifications
- Offline-first with background sync
- Team workspaces with granular permissions
- Integrations with Slack, Google, and Stripe
- Full-text search with smart filters
- Guided onboarding with ready-made templates

## Tech Stack
- **Frontend:** Vue 3
- **Backend:** FastAPI (Python)
- **Database:** SQLite
- **Infra/DevOps:** Docker + AWS ECS, GitHub Actions CI/CD

## Architecture
A Vue 3 client talks to a FastAPI (Python) API over REST. Data lives in SQLite. Background jobs handle async work, and the whole stack is containerized and deployed via Docker + AWS ECS.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
