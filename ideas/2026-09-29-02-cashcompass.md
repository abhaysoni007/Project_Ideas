# CashCompass
> Navigate your finances, accelerate your future.

## Problem
Most consumers lack real‑time visibility into how their discretionary spending affects their savings goals, leading to missed opportunities for higher‑impact investments. Manual budgeting is tedious, and generic financial tools rarely adapt to individual risk appetites.

## Target Users
- Millennials and Gen‑Z users who prefer digital financial management  
- Working professionals with multiple bank accounts and credit cards  
- Individuals planning for early retirement or large purchases  
- Users who want automated, risk‑aware savings without constant monitoring  

## Key Features
- Real‑time account aggregation across banks, credit cards, and investment platforms  
- Automatic surplus detection and reallocation based on user‑defined risk profiles  
- Dynamic portfolio suggestion engine that prioritizes high‑yield savings or diversified ETFs  
- Smart notifications for spending anomalies and rebalancing opportunities  
- Goal‑tracking dashboards with visual progress metrics  
- Secure, GDPR‑compliant data handling with end‑to‑end encryption  
- Voice‑activated assistant for quick account checks and transaction queries  

## Tech Stack
**Frontend**  
- React (Next.js) with TypeScript  
- Tailwind CSS for rapid UI development  

**Backend**  
- Node.js (Express) with TypeScript  
- GraphQL API (Apollo Server) for flexible data queries  

**Database**  
- PostgreSQL (primary relational store)  
- Redis (in‑memory cache for real‑time metrics)  

**Infra/DevOps**  
- Docker & Docker Compose for local dev, Kubernetes on GKE for production  
- Terraform for IaC, GitHub Actions CI/CD pipelines  
- Cloudflare CDN & Workers for edge caching  

**AI/ML**  
- Python microservice (FastAPI) for risk‑profile scoring using scikit‑learn models  
- TensorFlow Lite models for on‑device anomaly detection  

## Architecture
CashCompass follows a microservice architecture where the frontend consumes a GraphQL gateway that orchestrates calls to a Node.js backend, a Python AI service, and external banking APIs via the Plaid connector. Data is persisted in PostgreSQL, with Redis caching for high‑frequency financial metrics. The system is containerized and deployed on GKE, managed through Terraform, with CI/CD via GitHub Actions ensuring rapid, reliable releases.

## Roadmap
- **v1** – Core account aggregation, real‑time surplus detection, basic risk‑based reallocation, web dashboard  
- **v2** – Mobile app (React Native), AI‑driven investment suggestions, multi‑currency support, advanced goal‑tracking  
- **v3** – Voice assistant integration, partnership with robo‑advisors, automated tax‑loss harvesting, international expansion with localized regulations
