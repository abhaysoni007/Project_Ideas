# SkillSphere

> SkillSphere is an online learning platform for professionals and entrepreneurs, offering courses, workshops, and certification programs in various skills and industries.

## Problem
Creators struggle to organize their expenses without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Creators
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email and push notifications
- Usage analytics and an admin panel
- Audit log of every change
- One-click export to CSV and PDF
- Guided onboarding with ready-made templates
- Full-text search with smart filters

## Tech Stack
- **Frontend:** Flutter
- **Backend:** Go (Gin)
- **Database:** Supabase
- **Infra/DevOps:** Docker + AWS ECS, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a Go (Gin) API over REST. Data lives in Supabase. Background jobs handle async work, and the whole stack is containerized and deployed via Docker + AWS ECS.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
