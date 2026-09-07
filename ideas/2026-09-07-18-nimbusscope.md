# NimbusScope

> A CLI that detects unused dependencies across a monorepo and opens cleanup PRs.

## Problem
Remote workers struggle to personalize their energy usage without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Remote workers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Audit log of every change
- Offline-first with background sync
- Team workspaces with granular permissions
- Integrations with Slack, Google, and Stripe
- One-click export to CSV and PDF
- Full-text search with smart filters

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
