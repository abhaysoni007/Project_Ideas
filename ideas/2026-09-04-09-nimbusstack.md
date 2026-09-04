# NimbusStack

> A tool that audits a website's Core Web Vitals and suggests concrete fixes.

## Problem
Students struggle to cluster their recipes without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Students
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Guided onboarding with ready-made templates
- Integrations with Slack, Google, and Stripe
- Offline-first with background sync
- Full-text search with smart filters
- Usage analytics and an admin panel
- Responsive dashboard with light and dark mode

## Tech Stack
- **Frontend:** Vue 3
- **Backend:** Go (Gin)
- **Database:** SQLite
- **Infra/DevOps:** Docker + AWS ECS, GitHub Actions CI/CD

## Architecture
A Vue 3 client talks to a Go (Gin) API over REST. Data lives in SQLite. Background jobs handle async work, and the whole stack is containerized and deployed via Docker + AWS ECS.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
