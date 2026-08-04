# Artisan's Ally

> Empowers small-scale artisans and craftspeople to showcase and sell their products through a dedicated e-commerce platform and marketing tools

## Problem
Gamers struggle to cluster their screen time without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Gamers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Full-text search with smart filters
- Email/OAuth sign-in with role-based access control
- Responsive dashboard with light and dark mode
- Audit log of every change
- Offline-first with background sync
- Email and push notifications

## Tech Stack
- **Frontend:** Next.js
- **Backend:** Node.js + Express
- **Database:** SQLite
- **Infra/DevOps:** Vercel, GitHub Actions CI/CD

## Architecture
A Next.js client talks to a Node.js + Express API over REST. Data lives in SQLite. Background jobs handle async work, and the whole stack is containerized and deployed via Vercel.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
