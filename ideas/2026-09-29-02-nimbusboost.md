# NimbusBoost
> Rule‑based linter for accessible HTML emails – no AI, just clean code.

## Problem  
Many marketers send HTML emails that fail accessibility tests, causing poor user experience and potential regulatory issues. Existing linters are AI‑heavy, slow, and difficult to integrate into email‑building workflows.

## Target Users  
- Email marketers and copywriters  
- Front‑end developers building transactional email templates  
- QA teams ensuring compliance with WCAG 2.1 AA  
- Automation engineers integrating linting into CI pipelines  

## Key Features  
- **Rule‑based engine** that flags WCAG 2.1 AA violations specific to email contexts  
- **Custom rule set editor** for teams to add or tweak rules without code changes  
- **CLI and GitHub Action** for seamless CI/CD integration  
- **Real‑time editor plugin** (VS Code) with inline diagnostics  
- **Exportable reports** in JSON, HTML, and Markdown formats  
- **Performance‑optimized** – < 200 ms lint for 10 KB email templates  
- **No external API calls** – all logic runs locally for privacy  

## Tech Stack  
- **Frontend**  
  - React 18 + TypeScript  
  - Tailwind CSS for rapid styling  
- **Backend**  
  - Node.js 20 + Express for the linting API  
  - Typescript for type safety  
- **Database**  
  - PostgreSQL 15 (for rule persistence in enterprise mode)  
- **Infra/DevOps**  
  - Docker + Docker Compose for local dev  
  - Terraform + EKS for cloud deployment  
  - GitHub Actions for CI pipelines  
- **AI/ML**  
  - None (pure rule‑based logic)  

## Architecture  
NimbusBoost consists of a lightweight Node.js linting engine that parses email HTML, applies a curated set of accessibility rules, and returns diagnostics. The front‑end editor plugin communicates with the local engine via a WebSocket API. In enterprise mode, a PostgreSQL database stores custom rule definitions and linting history, while the cloud deployment is containerized and orchestrated with Kubernetes, managed through Terraform and monitored via Prometheus/ Grafana.  

## Roadmap  
- **v1** – Core rule engine, CLI, and VS Code plugin; basic rule set covering color contrast, alt text, and link semantics.  
- **v2** – Web UI for rule management, exportable reports, and GitHub Action integration; performance tuning for large templates.  
- **v3** – Enterprise features: rule persistence, role‑based access control, audit logs, and optional integration with email‑service‑providers (e.g., SendGrid, Mailchimp) for pre‑send linting.
