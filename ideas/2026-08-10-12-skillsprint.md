# SkillSprint

> provides an online learning platform that focuses on short, interactive, and project-based courses to help professionals develop in-demand skills and enhance their career prospects.

## Problem
Gamers struggle to organize their energy usage without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Gamers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- One-click export to CSV and PDF
- Email and push notifications
- Real-time updates over WebSockets
- Full-text search with smart filters
- AI-assisted recommendations and summaries
- Public REST API with scoped API keys

## Tech Stack
- **Frontend:** Vue 3
- **Backend:** NestJS
- **Database:** MongoDB
- **Infra/DevOps:** Railway, GitHub Actions CI/CD

## Architecture
A Vue 3 client talks to a NestJS API over REST. Data lives in MongoDB. Background jobs handle async work, and the whole stack is containerized and deployed via Railway.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
