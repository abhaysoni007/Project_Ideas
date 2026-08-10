# CampusConnect

> provides a social networking and community engagement platform for universities and colleges to foster student connection, collaboration, and campus involvement.

## Problem
Small teams struggle to audit their job applications without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Small teams
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- One-click export to CSV and PDF
- Guided onboarding with ready-made templates
- Responsive dashboard with light and dark mode
- Real-time updates over WebSockets
- Email/OAuth sign-in with role-based access control
- Full-text search with smart filters

## Tech Stack
- **Frontend:** Flutter
- **Backend:** NestJS
- **Database:** PostgreSQL
- **Infra/DevOps:** Railway, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a NestJS API over REST. Data lives in PostgreSQL. Background jobs handle async work, and the whole stack is containerized and deployed via Railway.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
