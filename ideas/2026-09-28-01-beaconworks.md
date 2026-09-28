# BeaconWorks

> A Pomodoro timer that mutes Slack and sets your calendar to busy automatically.

## Problem
Job seekers struggle to personalize their study material without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Job seekers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Full-text search with smart filters
- Team workspaces with granular permissions
- AI-assisted recommendations and summaries
- Audit log of every change
- Usage analytics and an admin panel
- Real-time updates over WebSockets

## Tech Stack
- **Frontend:** Flutter
- **Backend:** NestJS
- **Database:** Supabase
- **Infra/DevOps:** GCP Cloud Run, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a NestJS API over REST. Data lives in Supabase. Background jobs handle async work, and the whole stack is containerized and deployed via GCP Cloud Run.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
