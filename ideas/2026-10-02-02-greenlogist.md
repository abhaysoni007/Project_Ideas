# GreenLogist
> **Track, Verify, Reduce: Blockchain‑powered Recycling Route Optimization**

## Problem
Municipal waste agencies struggle to verify that recycling trucks follow designated low‑carbon routes, leading to excess emissions and costly inefficiencies. Current tracking systems lack transparency and immutable audit trails, making it hard to enforce compliance or reward eco‑friendly behavior.

## Target Users
- City and county waste management departments
- Contracted recycling fleet operators
- Environmental auditors and regulators
- Sustainability officers in municipalities

## Key Features
- **Real‑time GPS mapping** of truck routes with geofencing to enforce low‑carbon corridors  
- **Immutable route ledger** on a permissioned blockchain (Hyperledger Fabric) for tamper‑proof auditing  
- **Carbon footprint calculator** that aggregates emissions data from onboard OBD‑II interfaces  
- **Dynamic route optimization** powered by machine learning that adapts to traffic, weather, and load constraints  
- **Compliance dashboard** with alerts, scorecards, and incentives tied to verified savings  
- **API gateway** for integration with existing municipal IT stacks (e.g., GIS, ERP)  
- **Mobile app** for drivers to receive real‑time instructions and confirm route adherence

## Tech Stack
- **Frontend**
  - React 18 + Redux Toolkit
  - TypeScript
  - Ant Design for UI components
  - Mapbox GL JS for interactive maps
- **Backend**
  - Node.js 20 (Express) as API layer
  - NestJS for modular architecture
  - TypeScript
  - gRPC for micro‑service communication
- **Database**
  - PostgreSQL 15 (relational data, spatial extensions via PostGIS)
  - MongoDB 7 (unstructured logs, telemetry)
- **Infra/DevOps**
  - Kubernetes 1.30 on AWS EKS
  - Helm charts for deployment
  - Terraform for IaC
  - GitHub Actions CI/CD
  - Prometheus + Grafana for observability
  - HashiCorp Vault for secrets management
- **Blockchain**
  - Hyperledger Fabric 2.5 (permissioned network)
  - CouchDB 4.0 for state database
- **AI/ML**
  - Python 3.11 with FastAPI for ML micro‑service
  - PyTorch 2.0 for route optimization model
  - Scikit‑learn for anomaly detection in emissions data

## Architecture
GreenLogist follows a modular micro‑service architecture running on Kubernetes. The core services include **Vehicle Tracking**, **Emission Calculation**, **Route Optimization**, and **Blockchain Ledger**. Each service exposes RESTful or gRPC endpoints, and they communicate through a Kafka event bus. The blockchain network is anchored to a Hyperledger Fabric channel, with CouchDB backing the world state. Frontend dashboards consume aggregated data via GraphQL, while the mobile app uses WebSockets for live updates.

## Roadmap
- **v1**: MVP – GPS tracking, basic route ledger, carbon calculator, admin dashboard, single‑node blockchain deployment
- **v2**: Full fleet integration – dynamic optimization, driver mobile app, API gateway, multi‑node Fabric cluster, GDPR compliance
- **v3**: Enterprise scale – AI‑driven incentives, integration with city GIS, multi‑municipality federation, open API for third‑party eco‑apps
