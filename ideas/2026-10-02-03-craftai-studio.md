# CraftAI Studio  
> Turn ideas into physics‑rich levels in seconds.

## Problem  
Indie game devs spend hours hand‑crafting realistic physics assets and level geometry, which stalls iteration and increases time to market. Existing tools are either too generic or require deep technical expertise, creating a bottleneck in prototyping.

## Target Users  
- Indie game designers & solo devs  
- Small studio teams (≤10 people)  
- Prototypers in game jams or rapid concept testing  
- Educators teaching procedural level design  

## Key Features  
- **Instant physics asset generator**: AI‑driven creation of rigid bodies, soft bodies, and collision meshes from simple sketches.  
- **Procedural level layout**: Generate playable maps with varied terrain, obstacles, and physics interactions.  
- **Real‑time preview**: Interactive 3D viewport powered by WebGL and the Bullet physics engine.  
- **Asset library & versioning**: Store, tag, and revert physics assets and level templates.  
- **Export pipelines**: One‑click export to Unity, Unreal, or Godot.  
- **Collaborative workspace**: Live co‑editing with role‑based permissions.  
- **Performance profiling**: Visualize physics performance metrics during design.  

## Tech Stack  

- **Frontend**  
  - React 18 + TypeScript  
  - Vite for dev tooling  
  - Tailwind CSS & Radix UI  
  - Zustand for lightweight state management  

- **Backend**  
  - NestJS (Node.js) + TypeScript  
  - GraphQL (Apollo Server) for flexible queries  

- **Database**  
  - PostgreSQL 15  
  - Prisma ORM for type safety  

- **Infra/DevOps**  
  - Docker & Docker Compose for local dev  
  - Kubernetes (AWS EKS) for production scaling  
  - Terraform for IaC  
  - GitHub Actions for CI/CD pipeline  

- **AI/ML**  
  - PyTorch + TorchServe for inference microservice  
  - Hugging Face Transformers for text‑to‑level prompts  
  - Stable Diffusion (via Diffusers library) for texture generation  
  - Blender Python scripts for mesh export and physics baking  

## Architecture  
The system follows a micro‑service architecture: the React SPA communicates with a NestJS GraphQL API, which orchestrates calls to a dedicated AI inference service (PyTorch/TorchServe). Physics asset generation leverages Blender headless rendering and the Bullet physics library, with results stored in PostgreSQL. The entire stack is containerized and deployed on AWS EKS, with Terraform managing infrastructure. CI/CD pipelines ensure rapid iteration and automated testing.

## Roadmap  

- **v1** – Core web app, physics asset generator, procedural level layout, real‑time preview, export to Unity/Unreal.  
- **v2** – AI‑enhanced level design prompts, collaborative editing, asset library with versioning, performance profiling dashboard.  
- **v3** – VR preview mode, marketplace integration for user‑generated assets, advanced physics tuning, cross‑platform deployment (Web, Desktop, Mobile).
