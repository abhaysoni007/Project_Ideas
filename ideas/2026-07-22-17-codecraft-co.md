# CodeCraft Co

> creates interactive coding lessons and projects for kids, focusing on game development and robotics

## Problem
Job seekers struggle to benchmark their job applications without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Job seekers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Integrations with Slack, Google, and Stripe
- Offline-first with background sync
- Usage analytics and an admin panel
- AI-assisted recommendations and summaries
- Public REST API with scoped API keys
- One-click export to CSV and PDF

## Tech Stack
- **Frontend:** Vue 3
- **Backend:** Node.js + Express
- **Database:** MongoDB
- **Infra/DevOps:** Fly.io, GitHub Actions CI/CD

## Architecture
A Vue 3 client talks to a Node.js + Express API over REST. Data lives in MongoDB. Background jobs handle async work, and the whole stack is containerized and deployed via Fly.io.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
