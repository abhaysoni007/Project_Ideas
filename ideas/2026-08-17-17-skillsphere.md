# SkillSphere

> offers a professional training and development platform for enterprises to upskill and reskill their employees, track learning progress, and identify skill gaps.

## Problem
Job seekers struggle to organize their energy usage without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Job seekers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- One-click export to CSV and PDF
- AI-assisted recommendations and summaries
- Full-text search with smart filters
- Audit log of every change
- Public REST API with scoped API keys
- Guided onboarding with ready-made templates

## Tech Stack
- **Frontend:** React Native
- **Backend:** NestJS
- **Database:** SQLite
- **Infra/DevOps:** Fly.io, GitHub Actions CI/CD

## Architecture
A React Native client talks to a NestJS API over REST. Data lives in SQLite. Background jobs handle async work, and the whole stack is containerized and deployed via Fly.io.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
