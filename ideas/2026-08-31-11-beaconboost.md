# BeaconBoost

> A no-code builder for designers to translate energy usage without writing code.

## Problem
Gamers struggle to schedule their expenses without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Gamers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Guided onboarding with ready-made templates
- Integrations with Slack, Google, and Stripe
- One-click export to CSV and PDF
- Real-time updates over WebSockets
- Full-text search with smart filters
- Offline-first with background sync

## Tech Stack
- **Frontend:** Vue 3
- **Backend:** Go (Gin)
- **Database:** Supabase
- **Infra/DevOps:** GCP Cloud Run, GitHub Actions CI/CD

## Architecture
A Vue 3 client talks to a Go (Gin) API over REST. Data lives in Supabase. Background jobs handle async work, and the whole stack is containerized and deployed via GCP Cloud Run.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
