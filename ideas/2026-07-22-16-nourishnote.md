# NourishNote

> generates customized meal planning and grocery lists based on users' nutritional needs, dietary restrictions, and food preferences

## Problem
Developers struggle to organize their git commits without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Developers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email/OAuth sign-in with role-based access control
- Email and push notifications
- Public REST API with scoped API keys
- Team workspaces with granular permissions
- Full-text search with smart filters
- One-click export to CSV and PDF

## Tech Stack
- **Frontend:** Next.js
- **Backend:** NestJS
- **Database:** Supabase
- **Infra/DevOps:** GCP Cloud Run, GitHub Actions CI/CD

## Architecture
A Next.js client talks to a NestJS API over REST. Data lives in Supabase. Background jobs handle async work, and the whole stack is containerized and deployed via GCP Cloud Run.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
