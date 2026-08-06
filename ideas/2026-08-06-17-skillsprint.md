# SkillSprint

> provides a career development and upskilling platform for professionals and enterprises to enhance employee skills and adapt to changing workforce demands.

## Problem
Open-source maintainers struggle to audit their workout plans without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Open-source maintainers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- One-click export to CSV and PDF
- Usage analytics and an admin panel
- Full-text search with smart filters
- Real-time updates over WebSockets
- Email/OAuth sign-in with role-based access control
- Email and push notifications

## Tech Stack
- **Frontend:** Next.js
- **Backend:** Django
- **Database:** PostgreSQL
- **Infra/DevOps:** Docker + AWS ECS, GitHub Actions CI/CD

## Architecture
A Next.js client talks to a Django API over REST. Data lives in PostgreSQL. Background jobs handle async work, and the whole stack is containerized and deployed via Docker + AWS ECS.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
