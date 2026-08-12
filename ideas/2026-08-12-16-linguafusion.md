# LinguaFusion

> offers a language learning platform that combines AI-powered chatbots, virtual reality, and social learning to help users achieve fluency in a new language.

## Problem
Developers struggle to predict their code reviews without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Developers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email and push notifications
- Public REST API with scoped API keys
- Audit log of every change
- Full-text search with smart filters
- Integrations with Slack, Google, and Stripe
- Offline-first with background sync

## Tech Stack
- **Frontend:** Flutter
- **Backend:** Node.js + Express
- **Database:** MySQL
- **Infra/DevOps:** Docker + AWS ECS, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a Node.js + Express API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via Docker + AWS ECS.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
