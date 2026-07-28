# LinguaFusion

> helps language learners improve their skills with interactive, gamified lessons and language exchange opportunities with native speakers

## Problem
Job seekers struggle to personalize their API logs without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Job seekers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email and push notifications
- Integrations with Slack, Google, and Stripe
- One-click export to CSV and PDF
- Email/OAuth sign-in with role-based access control
- Responsive dashboard with light and dark mode
- Guided onboarding with ready-made templates

## Tech Stack
- **Frontend:** Flutter
- **Backend:** NestJS
- **Database:** MySQL
- **Infra/DevOps:** Vercel, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a NestJS API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via Vercel.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
