# NimbusStack

> A Slack/Discord bot that helps founders personalize travel itineraries without leaving chat.

## Problem
Open-source maintainers struggle to schedule their customer feedback without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Open-source maintainers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Public REST API with scoped API keys
- One-click export to CSV and PDF
- Team workspaces with granular permissions
- Responsive dashboard with light and dark mode
- Email/OAuth sign-in with role-based access control
- AI-assisted recommendations and summaries

## Tech Stack
- **Frontend:** SvelteKit
- **Backend:** Node.js + Express
- **Database:** PostgreSQL
- **Infra/DevOps:** Vercel, GitHub Actions CI/CD

## Architecture
A SvelteKit client talks to a Node.js + Express API over REST. Data lives in PostgreSQL. Background jobs handle async work, and the whole stack is containerized and deployed via Vercel.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
