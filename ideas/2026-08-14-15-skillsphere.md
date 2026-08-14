# SkillSphere

> enables students and professionals to develop new skills and competencies through a personalized learning and career development platform

## Problem
Freelancers struggle to track their invoices without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Freelancers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email and push notifications
- Public REST API with scoped API keys
- Full-text search with smart filters
- Usage analytics and an admin panel
- Team workspaces with granular permissions
- Integrations with Slack, Google, and Stripe

## Tech Stack
- **Frontend:** Flutter
- **Backend:** Go (Gin)
- **Database:** MySQL
- **Infra/DevOps:** Vercel, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a Go (Gin) API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via Vercel.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
