# NimbusStack

> A local-first note app where every note is a git commit you can diff over time.

## Problem
Developers struggle to translate their code reviews without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Developers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email/OAuth sign-in with role-based access control
- Offline-first with background sync
- Team workspaces with granular permissions
- Full-text search with smart filters
- AI-assisted recommendations and summaries
- Usage analytics and an admin panel

## Tech Stack
- **Frontend:** React
- **Backend:** Django
- **Database:** PostgreSQL
- **Infra/DevOps:** Railway, GitHub Actions CI/CD

## Architecture
A React client talks to a Django API over REST. Data lives in PostgreSQL. Background jobs handle async work, and the whole stack is containerized and deployed via Railway.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
