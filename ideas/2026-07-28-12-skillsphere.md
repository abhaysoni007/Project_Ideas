# SkillSphere

> connects professionals with experts and thought leaders in their industry, offering mentorship, coaching, and skills development opportunities

## Problem
Researchers struggle to audit their API logs without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Researchers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- One-click export to CSV and PDF
- Responsive dashboard with light and dark mode
- Full-text search with smart filters
- Team workspaces with granular permissions
- Guided onboarding with ready-made templates
- Audit log of every change

## Tech Stack
- **Frontend:** Flutter
- **Backend:** Node.js + Express
- **Database:** PostgreSQL
- **Infra/DevOps:** Railway, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a Node.js + Express API over REST. Data lives in PostgreSQL. Background jobs handle async work, and the whole stack is containerized and deployed via Railway.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
