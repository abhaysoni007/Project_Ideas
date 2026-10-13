# HealthNote AI
> Voice‑powered EHR: let the patient speak, we write the chart.

## Problem
Clinicians spend up to 30 % of their time on documentation, which reduces patient contact and increases burnout. Existing dictation tools are slow, error‑prone, and rarely map speech to structured EHR fields automatically. This manual lag delays care and introduces inconsistencies in chart data.

## Target Users
- Primary care physicians  
- Nurse practitioners and physician assistants  
- Clinical documentation specialists  
- Clinic and hospital IT teams

## Key Features
- **Real‑time voice capture** via WebRTC with noise suppression and echo cancellation  
- **Accurate transcription** using Whisper‑based models fine‑tuned on medical corpora  
- **NLP‑driven mapping** to structured EHR fields (ICD‑10, CPT, medication lists) via clinical BERT and spaCy pipelines  
- **HIPAA‑compliant secure storage** of audio, transcripts, and metadata in encrypted S3 buckets and Postgres  
- **Offline mode** with local edge inference for mobile devices (together with a fallback sync when connectivity returns)  
- **EHR integration** through FHIR APIs for seamless push to Epic, Cerner, or custom systems  
- **Audit trail & versioning** for every note with cryptographic hashes to satisfy regulatory requirements

## Tech Stack
- **Frontend**  
  - React 18 + TypeScript  
  - Tailwind CSS for rapid UI design  
  - WebRTC & MediaRecorder API for audio capture  
  - Redux Toolkit for state management  

- **Backend**  
  - NestJS (Node.js, TypeScript) for REST and gRPC services  
  - FastAPI (Python) microservice for AI inference  
  - WebSocket gateway for live transcription streams  

- **Database**  
  - PostgreSQL 15 (primary data store)  
  - TimescaleDB extension for time‑series audio metadata  
  - Redis 7 for caching and pub/sub  

- **Infra/DevOps**  
  - Docker + Docker Compose for local dev  
  - Kubernetes (EKS on AWS) for production scaling  
  - Terraform for IaC (VPC, IAM, RDS, EKS)  
  - GitHub Actions for CI/CD pipelines  
  - Prometheus + Grafana for observability  

- **AI/ML**  
  - Whisper‑X (OpenAI) fine‑tuned on MIMIC‑III for transcription  
  - Clinical BERT (BioBERT) + spaCy for entity extraction and slot filling  
  - LangChain integration for prompt‑based reasoning and validation  
  - ONNX Runtime for low‑latency inference on edge devices  

## Architecture
HealthNote AI follows a modular microservices architecture. The React client streams audio via WebRTC to the NestJS gateway, which forwards data to the FastAPI inference service. Transcripts are returned in real time and stored in PostgreSQL, while structured entities are mapped to FHIR bundles and pushed to the target EHR system. All services run in Kubernetes pods with sidecar Envoy for secure service‑mesh communication, and data at rest is encrypted with AWS KMS. Continuous monitoring and automated scaling ensure low latency and high availability.

## Roadmap
- **v1** – MVP: voice capture, Whisper transcription, basic ICD‑10 mapping, FHIR push, HIPAA‑compliant storage.  
- **v2** – Enhanced NLP: medication & vitals extraction, multi‑language support, offline edge inference, audit trail UI.  
- **v3** – Enterprise features: role‑based access control, audit logging, AI‑driven note completion suggestions, integration with additional EHR vendors, performance tuning for 10,000 concurrent users.
