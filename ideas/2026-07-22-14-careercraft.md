# CareerCraft

> helps students and recent graduates develop essential skills and build professional portfolios through interactive workshops and mentorship programs

## Problem
Freelancers struggle to automate their screen time without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Freelancers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email/OAuth sign-in with role-based access control
- Team workspaces with granular permissions
- Integrations with Slack, Google, and Stripe
- Usage analytics and an admin panel
- Guided onboarding with ready-made templates
- Audit log of every change

## Tech Stack
- **Frontend:** Vue 3
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Infra/DevOps:** Fly.io, GitHub Actions CI/CD

## Architecture
A Vue 3 client talks to a FastAPI (Python) API over REST. Data lives in PostgreSQL. Background jobs handle async work, and the whole stack is containerized and deployed via Fly.io.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
