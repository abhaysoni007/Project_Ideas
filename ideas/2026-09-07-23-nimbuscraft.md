# NimbusCraft

> A local-first note app where every note is a git commit you can diff over time.

## Problem
Designers struggle to predict their API logs without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Designers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Audit log of every change
- Usage analytics and an admin panel
- AI-assisted recommendations and summaries
- Team workspaces with granular permissions
- Integrations with Slack, Google, and Stripe
- Offline-first with background sync

## Tech Stack
- **Frontend:** React Native
- **Backend:** Go (Gin)
- **Database:** MySQL
- **Infra/DevOps:** GCP Cloud Run, GitHub Actions CI/CD

## Architecture
A React Native client talks to a Go (Gin) API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via GCP Cloud Run.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
