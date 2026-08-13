# CulinaryGenie

> generates recipe suggestions based on users' dietary preferences, ingredient availability, and cooking skills, with step-by-step video instructions.

## Problem
Open-source maintainers struggle to benchmark their expenses without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Open-source maintainers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Real-time updates over WebSockets
- Full-text search with smart filters
- Team workspaces with granular permissions
- Guided onboarding with ready-made templates
- Offline-first with background sync
- AI-assisted recommendations and summaries

## Tech Stack
- **Frontend:** SvelteKit
- **Backend:** NestJS
- **Database:** PostgreSQL
- **Infra/DevOps:** GCP Cloud Run, GitHub Actions CI/CD

## Architecture
A SvelteKit client talks to a NestJS API over REST. Data lives in PostgreSQL. Background jobs handle async work, and the whole stack is containerized and deployed via GCP Cloud Run.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
