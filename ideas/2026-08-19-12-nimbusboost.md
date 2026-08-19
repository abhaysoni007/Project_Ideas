# NimbusBoost

> A self-hosted tool that lets developers organize study material with full data privacy.

## Problem
Teachers struggle to predict their workout plans without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Teachers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email and push notifications
- Real-time updates over WebSockets
- Guided onboarding with ready-made templates
- One-click export to CSV and PDF
- Offline-first with background sync
- Team workspaces with granular permissions

## Tech Stack
- **Frontend:** SvelteKit
- **Backend:** Django
- **Database:** MySQL
- **Infra/DevOps:** Vercel, GitHub Actions CI/CD

## Architecture
A SvelteKit client talks to a Django API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via Vercel.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
