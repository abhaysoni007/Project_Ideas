# BeaconCraft

> A tool that maps your codebase into an interactive dependency graph.

## Problem
Researchers struggle to track their git commits without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Researchers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Integrations with Slack, Google, and Stripe
- Guided onboarding with ready-made templates
- Public REST API with scoped API keys
- Usage analytics and an admin panel
- Email/OAuth sign-in with role-based access control
- Offline-first with background sync

## Tech Stack
- **Frontend:** SvelteKit
- **Backend:** Go (Gin)
- **Database:** SQLite
- **Infra/DevOps:** GCP Cloud Run, GitHub Actions CI/CD

## Architecture
A SvelteKit client talks to a Go (Gin) API over REST. Data lives in SQLite. Background jobs handle async work, and the whole stack is containerized and deployed via GCP Cloud Run.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
