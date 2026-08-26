# NimbusBoost

> A mobile app that gamifies travel itineraries to keep job seekers engaged.

## Problem
Developers struggle to track their daily habits without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Developers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email and push notifications
- Public REST API with scoped API keys
- Usage analytics and an admin panel
- Responsive dashboard with light and dark mode
- Audit log of every change
- Guided onboarding with ready-made templates

## Tech Stack
- **Frontend:** Flutter
- **Backend:** Django
- **Database:** PostgreSQL
- **Infra/DevOps:** GCP Cloud Run, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a Django API over REST. Data lives in PostgreSQL. Background jobs handle async work, and the whole stack is containerized and deployed via GCP Cloud Run.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
