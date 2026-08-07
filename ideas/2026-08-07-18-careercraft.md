# CareerCraft

> offers a professional development platform that provides personalized career coaching, resume building, and job matching services.

## Problem
Students struggle to recommend their meeting notes without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Students
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Audit log of every change
- AI-assisted recommendations and summaries
- Usage analytics and an admin panel
- Integrations with Slack, Google, and Stripe
- Guided onboarding with ready-made templates
- One-click export to CSV and PDF

## Tech Stack
- **Frontend:** Next.js
- **Backend:** Django
- **Database:** MongoDB
- **Infra/DevOps:** Vercel, GitHub Actions CI/CD

## Architecture
A Next.js client talks to a Django API over REST. Data lives in MongoDB. Background jobs handle async work, and the whole stack is containerized and deployed via Vercel.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
