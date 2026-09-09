# NimbusPilot

> An app that converts long YouTube tutorials into step-by-step markdown notes.

## Problem
Startups struggle to predict their workout plans without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Startups
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Responsive dashboard with light and dark mode
- AI-assisted recommendations and summaries
- Usage analytics and an admin panel
- Offline-first with background sync
- Team workspaces with granular permissions
- Real-time updates over WebSockets

## Tech Stack
- **Frontend:** Flutter
- **Backend:** FastAPI (Python)
- **Database:** MongoDB
- **Infra/DevOps:** Railway, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a FastAPI (Python) API over REST. Data lives in MongoDB. Background jobs handle async work, and the whole stack is containerized and deployed via Railway.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
