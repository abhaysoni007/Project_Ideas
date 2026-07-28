# WellnessWise

> provides individuals with a personalized wellness and self-care platform, offering guided meditations, mood tracking, and health advice

## Problem
Parents struggle to visualize their podcast highlights without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Parents
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Usage analytics and an admin panel
- Email and push notifications
- Team workspaces with granular permissions
- Offline-first with background sync
- AI-assisted recommendations and summaries
- Guided onboarding with ready-made templates

## Tech Stack
- **Frontend:** React Native
- **Backend:** NestJS
- **Database:** Supabase
- **Infra/DevOps:** Vercel, GitHub Actions CI/CD

## Architecture
A React Native client talks to a NestJS API over REST. Data lives in Supabase. Background jobs handle async work, and the whole stack is containerized and deployed via Vercel.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
