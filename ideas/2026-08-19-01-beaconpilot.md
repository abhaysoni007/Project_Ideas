# BeaconPilot

> A self-hosted tool that lets job seekers automate cloud costs with full data privacy.

## Problem
Creators struggle to audit their git commits without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Creators
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Audit log of every change
- One-click export to CSV and PDF
- Real-time updates over WebSockets
- Public REST API with scoped API keys
- Email/OAuth sign-in with role-based access control
- Team workspaces with granular permissions

## Tech Stack
- **Frontend:** SvelteKit
- **Backend:** Node.js + Express
- **Database:** Supabase
- **Infra/DevOps:** Vercel, GitHub Actions CI/CD

## Architecture
A SvelteKit client talks to a Node.js + Express API over REST. Data lives in Supabase. Background jobs handle async work, and the whole stack is containerized and deployed via Vercel.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
