# HomeCharge Hub
> Turn idle appliances into profit and resilience

## Problem
Many households have appliances that sit idle during off‑peak hours, wasting potential energy and failing to help balance the grid. Homeowners miss out on passive revenue opportunities, while utilities struggle to maintain grid stability without deploying costly infrastructure.

## Target Users
- Tech‑savvy homeowners looking to offset electricity bills
- Homeowners in areas with high peak‑hour demand charges
- Utilities seeking distributed energy resources for grid balancing
- Property managers of multi‑unit dwellings

## Key Features
- **Smart Appliance Integration** – connect via Wi‑Fi, Zigbee, or Z‑Wave and monitor usage in real time
- **Dynamic Load Balancing** – algorithmically shift appliance cycles to off‑peak or demand‑response periods
- **Passive Revenue Dashboard** – track credits earned through grid service participation
- **Automated Firmware Updates** – secure OTA updates for all connected modules
- **Regulatory Compliance Layer** – built‑in support for NERC CIP, ISO‑NE, and local incentive programs
- **Edge Gateway** – local data caching and MQTT broker for low‑latency control
- **Open API** – allow third‑party apps and utilities to integrate with HomeCharge Hub

## Tech Stack
- **Frontend**
  - React 18, Vite, TypeScript, Tailwind CSS
- **Backend**
  - NestJS, TypeScript, GraphQL
- **Database**
  - PostgreSQL, Redis (caching)
- **Infra/DevOps**
  - Docker, Kubernetes (EKS on AWS), Helm, Terraform, GitHub Actions CI/CD
- **AI/ML**
  - Python, TensorFlow, FastAPI, Docker

## Architecture
HomeCharge Hub follows a microservices architecture where the **Edge Gateway** runs locally on a Raspberry Pi or dedicated hub, exposing an MQTT broker to appliances. The **Backend Service** ingests telemetry, runs load‑balancing and revenue‑optimization algorithms, and exposes a GraphQL API for the web client. Data is persisted in PostgreSQL with Redis for real‑time state. Kubernetes orchestrates services in the cloud, while Terraform manages infrastructure. AI/ML models predict demand patterns and optimize appliance scheduling.

## Roadmap
- **v1**
  - Appliance onboarding via Zigbee/Z‑Wave
  - Basic load‑balancing scheduler
  - Web dashboard with revenue tracking
  - Secure OTA firmware updates
- **v2**
  - AI‑driven predictive scheduling
  - Integration with utility DSM programs
  - Mobile app (React Native)
  - Advanced analytics and reporting
- **v3**
  - Multi‑home aggregation for community‑level grid services
  - Real‑time bidding on energy markets
  - Expand to EV chargers and HVAC systems
  - Open API for third‑party ecosystem growth
