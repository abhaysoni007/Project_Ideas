# GamifyLearn  
> **Turn classroom moments into thrilling learning quests**

## Problem  
Students often find traditional quizzes tedious, which hampers engagement and retention.  
Teachers lack a flexible, reward‑based platform that blends gamification with curriculum standards, making it hard to create interactive assessments that feel like games.

## Target Users  
- K‑12 teachers seeking engaging assessment tools  
- School administrators looking for scalable, curriculum‑aligned solutions  
- Parents wanting to monitor and encourage their child’s learning progress  
- Educational content creators who want to monetize quiz modules  

## Key Features  
- **Drag‑and‑drop quiz builder** with instant preview and grading logic  
- **Reward system**: points, badges, and unlockable content that syncs with the classroom leaderboard  
- **Real‑time multiplayer mode** for collaborative problem solving and friendly competition  
- **AI‑powered quiz generator**: auto‑create question banks from lesson outlines (OpenAI API)  
- **Marketplace**: teachers can publish, sell, or share quizzes, with revenue sharing  
- **Analytics dashboard**: student performance, question difficulty, engagement metrics  
- **LMS integration** (Google Classroom, Canvas) for seamless data exchange  

## Tech Stack  
- **Frontend**: React 18, Next.js, TypeScript, Tailwind CSS, Recoil for state  
- **Backend**: NestJS (Node 14+), GraphQL, WebSocket (Socket.io)  
- **Database**: PostgreSQL 15, Prisma ORM, Redis for caching & pub/sub  
- **Infra/DevOps**: Docker, Kubernetes (EKS), Terraform, GitHub Actions CI/CD, CloudWatch  
- **AI/ML**: OpenAI GPT‑4 (question generation), TensorFlow Lite for in‑browser hint generation  

## Architecture  
GamifyLearn follows a micro‑service architecture: the **frontend** consumes a **GraphQL API** exposed by the **backend** service, which in turn orchestrates domain services (quiz logic, reward engine, marketplace). Real‑time interactions are handled by a dedicated **WebSocket service** that publishes events to Redis, enabling instant leaderboard updates. All services run in containers on Kubernetes, with Terraform provisioning AWS resources. AI‑related workloads are off‑loaded to a separate **AI microservice** that calls the OpenAI API and caches results in Redis.

## Roadmap  
- **v1** – Core quiz builder, point system, basic multiplayer, LMS integration, initial marketplace  
- **v2** – AI‑generated quizzes, advanced analytics, teacher collaboration tools, mobile web support  
- **v3** – Full marketplace monetization, cross‑school leaderboards, offline mode, AI‑driven adaptive learning paths
