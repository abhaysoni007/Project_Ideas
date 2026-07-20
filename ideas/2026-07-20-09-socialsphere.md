# SocialSphere

> helps small businesses and influencers manage their social media presence and engagement through a centralized platform with scheduling, analytics, and content creation tools.

## Problem
Parents struggle to audit their workout plans without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Parents
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Responsive dashboard with light and dark mode
- Full-text search with smart filters
- Email/OAuth sign-in with role-based access control
- Integrations with Slack, Google, and Stripe
- AI-assisted recommendations and summaries
- Audit log of every change

## Tech Stack
- **Frontend:** SvelteKit
- **Backend:** Django
- **Database:** MySQL
- **Infra/DevOps:** Fly.io, GitHub Actions CI/CD

## Architecture
A SvelteKit client talks to a Django API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via Fly.io.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
