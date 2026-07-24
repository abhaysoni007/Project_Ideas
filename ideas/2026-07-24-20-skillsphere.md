# SkillSphere

> Offers AI-driven career development and upskilling recommendations for professionals, using machine learning analysis of job market trends and required skills

## Problem
Gamers struggle to predict their expenses without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Gamers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Responsive dashboard with light and dark mode
- Integrations with Slack, Google, and Stripe
- Public REST API with scoped API keys
- Email/OAuth sign-in with role-based access control
- Usage analytics and an admin panel
- Audit log of every change

## Tech Stack
- **Frontend:** SvelteKit
- **Backend:** Node.js + Express
- **Database:** MySQL
- **Infra/DevOps:** GCP Cloud Run, GitHub Actions CI/CD

## Architecture
A SvelteKit client talks to a Node.js + Express API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via GCP Cloud Run.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
