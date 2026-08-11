# CulinaryCraft

> provides a meal planning, grocery delivery, and cooking education service for home cooks and professional chefs.

## Problem
Freelancers struggle to visualize their API logs without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Freelancers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Responsive dashboard with light and dark mode
- One-click export to CSV and PDF
- Guided onboarding with ready-made templates
- Integrations with Slack, Google, and Stripe
- Email and push notifications
- Offline-first with background sync

## Tech Stack
- **Frontend:** Next.js
- **Backend:** Node.js + Express
- **Database:** MySQL
- **Infra/DevOps:** Vercel, GitHub Actions CI/CD

## Architecture
A Next.js client talks to a Node.js + Express API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via Vercel.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
