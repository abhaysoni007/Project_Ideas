# CivicConnect

> develops a civic engagement platform for citizens to participate in local government decision-making, track community issues, and access public services.

## Problem
Founders struggle to automate their API logs without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Founders
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Team workspaces with granular permissions
- Guided onboarding with ready-made templates
- Integrations with Slack, Google, and Stripe
- AI-assisted recommendations and summaries
- Responsive dashboard with light and dark mode
- Audit log of every change

## Tech Stack
- **Frontend:** Flutter
- **Backend:** Node.js + Express
- **Database:** MongoDB
- **Infra/DevOps:** Fly.io, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a Node.js + Express API over REST. Data lives in MongoDB. Background jobs handle async work, and the whole stack is containerized and deployed via Fly.io.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
