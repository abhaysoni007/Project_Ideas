# CampusConnect

> Facilitates networking and community building among students, alumni, and faculty by providing

## Problem
Startups struggle to translate their sensor data without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Startups
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Full-text search with smart filters
- Responsive dashboard with light and dark mode
- Integrations with Slack, Google, and Stripe
- Email and push notifications
- Real-time updates over WebSockets
- Guided onboarding with ready-made templates

## Tech Stack
- **Frontend:** Flutter
- **Backend:** Node.js + Express
- **Database:** SQLite
- **Infra/DevOps:** Fly.io, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a Node.js + Express API over REST. Data lives in SQLite. Background jobs handle async work, and the whole stack is containerized and deployed via Fly.io.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
