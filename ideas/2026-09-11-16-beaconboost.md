# BeaconBoost

> A tool that maps your codebase into an interactive dependency graph.

## Problem
Teachers struggle to benchmark their code reviews without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Teachers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Guided onboarding with ready-made templates
- One-click export to CSV and PDF
- Usage analytics and an admin panel
- Offline-first with background sync
- Responsive dashboard with light and dark mode
- Integrations with Slack, Google, and Stripe

## Tech Stack
- **Frontend:** SvelteKit
- **Backend:** NestJS
- **Database:** MongoDB
- **Infra/DevOps:** Railway, GitHub Actions CI/CD

## Architecture
A SvelteKit client talks to a NestJS API over REST. Data lives in MongoDB. Background jobs handle async work, and the whole stack is containerized and deployed via Railway.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
