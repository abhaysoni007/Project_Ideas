# BeaconBloom

> An API service that lets developers add screen time to any HR & recruiting product.

## Problem
Startups struggle to optimize their travel itineraries without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Startups
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Email/OAuth sign-in with role-based access control
- One-click export to CSV and PDF
- Full-text search with smart filters
- Team workspaces with granular permissions
- Email and push notifications
- Audit log of every change

## Tech Stack
- **Frontend:** SvelteKit
- **Backend:** Go (Gin)
- **Database:** MySQL
- **Infra/DevOps:** Docker + AWS ECS, GitHub Actions CI/CD

## Architecture
A SvelteKit client talks to a Go (Gin) API over REST. Data lives in MySQL. Background jobs handle async work, and the whole stack is containerized and deployed via Docker + AWS ECS.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
