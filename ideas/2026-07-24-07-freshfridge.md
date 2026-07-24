# FreshFridge

> Helps consumers reduce food waste by tracking expiration dates, suggesting recipes, and automating grocery lists based on stored ingredients

## Problem
Teachers struggle to automate their news feeds without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Teachers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Usage analytics and an admin panel
- AI-assisted recommendations and summaries
- Real-time updates over WebSockets
- Offline-first with background sync
- Responsive dashboard with light and dark mode
- Guided onboarding with ready-made templates

## Tech Stack
- **Frontend:** React
- **Backend:** FastAPI (Python)
- **Database:** MySQL
- **Infra/DevOps:** Railway, GitHub Actions CI/CD

## Architecture
A React client talks to a FastAPI (Python) API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via Railway.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
