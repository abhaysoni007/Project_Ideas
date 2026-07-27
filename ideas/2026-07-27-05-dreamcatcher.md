# Dreamcatcher
> Empowering student well-being through AI-driven mental health support
## Problem
Mental health issues are increasingly prevalent among students, with many struggling to access support due to stigma, limited resources, or long wait times. This can lead to decreased academic performance, social isolation, and increased risk of mental health crises. Effective and accessible support systems are crucial to mitigating these issues.
## Target Users
* Students aged 16-25 in secondary and higher education institutions
* School counselors and mental health professionals
* Educators and administrators seeking to promote student well-being
## Key Features
* Conversational AI chatbot for students to discuss mental health concerns
* Personalized coping strategies and resource recommendations
* Integration with existing student information systems for seamless support
* Anonymous usage options to encourage honest disclosures
* Regular mood and sentiment analysis for proactive support
* Customizable chatbot personas to cater to diverse student populations
## Tech Stack
### Frontend
* React for building the chat interface and user dashboard
* Material-UI for responsive and accessible design
### Backend
* Node.js with Express.js for API management and server-side logic
* GraphQL for efficient data querying and schema management
### Database
* MongoDB for storing user data, chat transcripts, and analytics
* PostgreSQL for relational data management and reporting
### Infra/DevOps
* Docker for containerization and deployment
* Kubernetes for orchestration and scalability
* AWS for cloud hosting and infrastructure services
### AI/ML
* TensorFlow.js for client-side machine learning and natural language processing
* IBM Watson Assistant for AI-powered chatbot development
## Architecture
The Dreamcatcher architecture will consist of a microservices-based design, with separate services for the chatbot, user management, and analytics. The chatbot service will utilize TensorFlow.js for client-side ML and IBM Watson Assistant for AI-driven conversational logic. The user management service will handle authentication, authorization, and data storage using MongoDB and PostgreSQL. The analytics service will provide insights into user engagement, sentiment, and support outcomes.
## Roadmap
* v1: Develop and deploy the initial chatbot platform with basic features and integrate with a pilot school
* v2: Enhance the chatbot with personalized coping strategies, mood analysis, and anonymous usage options, and expand to 10 schools
* v3: Introduce customizable chatbot personas, advanced AI-driven support, and seamless integration with student information systems, with a goal of reaching 100 schools and universities
