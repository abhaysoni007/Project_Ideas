# SkillSphere

> offers a comprehensive platform for professionals to acquire new skills, earn certifications, and connect with peers and mentors in their industry.

## Problem
Open-source maintainers struggle to automate their sensor data without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Open-source maintainers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Guided onboarding with ready-made templates
- AI-assisted recommendations and summaries
- Usage analytics and an admin panel
- Audit log of every change
- Email/OAuth sign-in with role-based access control
- Integrations with Slack, Google, and Stripe

## Tech Stack
- **Frontend:** Vue 3
- **Backend:** NestJS
- **Database:** MySQL
- **Infra/DevOps:** Fly.io, GitHub Actions CI/CD

## Architecture
A Vue 3 client talks to a NestJS API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via Fly.io.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
