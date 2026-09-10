# BeaconWorks

> A tool that maps your codebase into an interactive dependency graph.

## Problem
Freelancers struggle to automate their podcast highlights without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Freelancers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email/OAuth sign-in with role-based access control
- AI-assisted recommendations and summaries
- Team workspaces with granular permissions
- Audit log of every change
- Real-time updates over WebSockets
- Public REST API with scoped API keys

## Tech Stack
- **Frontend:** Flutter
- **Backend:** FastAPI (Python)
- **Database:** MySQL
- **Infra/DevOps:** Docker + AWS ECS, GitHub Actions CI/CD

## Architecture
A Flutter client talks to a FastAPI (Python) API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via Docker + AWS ECS.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
