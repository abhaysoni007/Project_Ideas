# FreshFridge

> helps reduce food waste by providing meal planning, grocery management, and expiration date tracking for households and individuals.

## Problem
Job seekers struggle to benchmark their customer feedback without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Job seekers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Full-text search with smart filters
- Offline-first with background sync
- Email and push notifications
- Usage analytics and an admin panel
- Public REST API with scoped API keys
- AI-assisted recommendations and summaries

## Tech Stack
- **Frontend:** React Native
- **Backend:** Go (Gin)
- **Database:** Supabase
- **Infra/DevOps:** Vercel, GitHub Actions CI/CD

## Architecture
A React Native client talks to a Go (Gin) API over REST. Data lives in Supabase. Background jobs handle async work, and the whole stack is containerized and deployed via Vercel.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
