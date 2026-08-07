# MindfulMood

> develops a mental health and wellness app that uses AI-driven mood tracking and personalized mindfulness exercises to support emotional well-being.

## Problem
Designers struggle to recommend their travel itineraries without switching between too many disconnected tools. Existing options are either too generic or too expensive for their needs.

## Target Users
- Designers
- Small teams and startups
- Anyone who needs a focused, no-friction tool

## Key Features
- Responsive dashboard with light and dark mode
- Audit log of every change
- AI-assisted recommendations and summaries
- One-click export to CSV and PDF
- Email and push notifications
- Real-time updates over WebSockets

## Tech Stack
- **Frontend:** React
- **Backend:** NestJS
- **Database:** PostgreSQL
- **Infra/DevOps:** Railway, GitHub Actions CI/CD

## Architecture
A React client talks to a NestJS API over REST. Data lives in PostgreSQL. Background jobs handle async work, and the whole stack is containerized and deployed via Railway.

## Roadmap
- **v1** — Core flow, auth, and the dashboard
- **v2** — Integrations, notifications, and the public API
- **v3** — Team features, analytics, and mobile support
