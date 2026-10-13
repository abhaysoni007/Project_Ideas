# EcoRoute Planner  
> Reroute smarter, travel cleaner.

## Problem  
Urban commuters face rising congestion and rising emissions, yet most transit apps treat routes as static.  
Public transport operators lack real‑time insights to dynamically shift demand, leading to inefficient capacity usage.  
There is no single platform that balances speed, environmental impact, and multimodal options for eco‑conscious riders.

## Target Users  
- Eco‑conscious commuters who want lower‑impact travel options  
- City planners and transit agencies seeking congestion analytics  
- Bike‑share operators looking to integrate with public transport data  
- Local businesses interested in reducing delivery emissions  

## Key Features  
- Real‑time congestion heat maps using live traffic feeds  
- Dynamic multimodal routing (bus, subway, bike‑share, walking) with emission scores  
- Predictive traffic modeling to reroute before congestion builds  
- Community feedback loop for reporting delays or bike‑share station status  
- Offline mode with pre‑downloaded maps and last known routes  
- API for partners to embed routing and analytics into their services  
- Gamified carbon‑saving badge system to encourage sustainable choices  

## Tech Stack  
- **Frontend**  
  - React Native with Expo (cross‑platform mobile)  
  - TypeScript + Redux Toolkit for state management  
  - React Navigation for screen routing  
- **Backend**  
  - Node.js (TypeScript) with Express for REST endpoints  
  - Apollo Server (GraphQL) for flexible data queries  
- **Database**  
  - PostgreSQL with PostGIS for spatial queries and routing data  
  - Redis for caching frequent route lookups  
- **Infra/DevOps**  
  - Docker & Docker Compose for local dev, Kubernetes on AWS EKS for production  
  - GitHub Actions CI/CD pipelines, Terraform for IaC  
  - Prometheus + Grafana for monitoring, Loki for logs  
- **AI/ML**  
  - Python FastAPI microservice for predictive traffic modeling (scikit‑learn)  
  - TensorFlow Lite model for on‑device routing suggestions in low‑bandwidth scenarios  

## Architecture  
The system is a microservice‑based architecture. An API gateway (AWS API Gateway) fronts all services, authenticating via JWT issued by an Auth Service (Keycloak). The Routing Service consumes real‑time traffic streams from city sensors and bike‑share APIs, stores spatial data in PostGIS, and serves route calculations via GraphQL. A separate Prediction Service runs nightly ML jobs to update congestion forecasts, exposing results through a Redis cache for low‑latency lookup. The mobile client consumes these APIs, rendering interactive maps with Mapbox GL, while offline mode falls back to cached tiles and last known routes. All services are containerized, deployed to Kubernetes, and monitored with Prometheus/Grafana.

## Roadmap  
- **v1** – Core routing, live traffic integration, basic UI, single‑mode bus/subway support.  
- **v2** – Add bike‑share and walking options, AI‑driven congestion predictions, partner API, offline mode.  
- **v3** – Personalization engine, carbon‑impact gamification, city‑wide analytics dashboard, open data portal.
