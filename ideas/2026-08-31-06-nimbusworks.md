# NimbusWorks

> A CLI that turns terminal session recordings into shareable animated SVGs.

## Problem
Founders struggle to automate their recipes without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Founders
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Integrations with Slack, Google, and Stripe
- Email/OAuth sign-in with role-based access control
- Audit log of every change
- Usage analytics and an admin panel
- Responsive dashboard with light and dark mode
- Guided onboarding with ready-made templates

## Tech Stack
- **Frontend:** React
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Infra/DevOps:** Docker + AWS ECS, GitHub Actions CI/CD

## Architecture
A React client talks to a FastAPI (Python) API over REST. Data lives in PostgreSQL. Background jobs handle async work, and the whole stack is containerized and deployed via Docker + AWS ECS.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
