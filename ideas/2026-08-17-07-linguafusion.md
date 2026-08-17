# LinguaFusion

> offers an immersive language learning experience through interactive games, videos, and virtual reality simulations for individual learners and language schools.

## Problem
Teachers struggle to summarize their reading lists without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Teachers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email/OAuth sign-in with role-based access control
- Responsive dashboard with light and dark mode
- One-click export to CSV and PDF
- Offline-first with background sync
- Email and push notifications
- Usage analytics and an admin panel

## Tech Stack
- **Frontend:** React
- **Backend:** Go (Gin)
- **Database:** PostgreSQL
- **Infra/DevOps:** Vercel, GitHub Actions CI/CD

## Architecture
A React client talks to a Go (Gin) API over REST. Data lives in PostgreSQL. Background jobs handle async work, and the whole stack is containerized and deployed via Vercel.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
