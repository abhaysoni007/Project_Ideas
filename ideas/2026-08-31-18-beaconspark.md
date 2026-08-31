# BeaconSpark

> A habit tracker that pairs you with an accountability buddy who has the same goal.

## Problem
Creators struggle to optimize their invoices without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Creators
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Real-time updates over WebSockets
- Offline-first with background sync
- Guided onboarding with ready-made templates
- Email/OAuth sign-in with role-based access control
- Responsive dashboard with light and dark mode
- One-click export to CSV and PDF

## Tech Stack
- **Frontend:** Flutter
- **Backend:** FastAPI (Python)
- **Database:** SQLite
- **Infra/DevOps:** Docker + AWS ECS, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a FastAPI (Python) API over REST. Data lives in SQLite. Background jobs handle async work, and the whole stack is containerized and deployed via Docker + AWS ECS.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
