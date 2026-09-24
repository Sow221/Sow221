<a href="https://portefolio-ms.vercel.app">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Sow221/Sow221/main/assets/banner-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Sow221/Sow221/main/assets/banner-light.svg">
    <img alt="Sow221 — Software Engineering · Information Systems · Data & AI" src="https://raw.githubusercontent.com/Sow221/Sow221/main/assets/banner-light.svg">
  </picture>
</a>

<p align="center">
  <a href="https://portefolio-ms.vercel.app">
    <img src="https://img.shields.io/badge/Portfolio-111111?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio"/>
  </a>
  <a href="https://www.linkedin.com/in/ms-officiel/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="https://cif-credit-intelligence.onrender.com/docs">
    <img src="https://img.shields.io/badge/Live_API-111111?style=for-the-badge&logo=swagger&logoColor=white" alt="Live API documentation"/>
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Software_Engineering-111111?style=flat-square" alt="Software Engineering"/>
  <img src="https://img.shields.io/badge/Information_Systems-111111?style=flat-square" alt="Information Systems"/>
  <img src="https://img.shields.io/badge/Data_%26_AI-111111?style=flat-square" alt="Data and AI"/>
  <img src="https://img.shields.io/badge/Dakar%2C_Senegal-111111?style=flat-square" alt="Dakar, Senegal"/>
</p>

Software engineer building digital systems across applications, data and AI.

---

## 01 · Selected work

### CIF Credit Engine

**Credit-risk engineering platform · Open source**

A credit-risk engineering system for microfinance, built as a **reproducible ML system rather than a notebook**.

| Area                                                                                                                           | Implementation                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/git-branch-16.svg" width="16" alt=""/> Data & pipelines | DVC + Dagster                                                                        |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/graph-16.svg" width="16" alt=""/> ML                    | XGBoost + MLflow + model tracking                                                    |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/database-16.svg" width="16" alt=""/> Validation         | Method validated on public Lending Club data with an out-of-time evaluation protocol |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/shield-check-16.svg" width="16" alt=""/> API & security | FastAPI + JWT authentication + rate limiting                                         |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/database-16.svg" width="16" alt=""/> Persistence        | PostgreSQL + audit logging                                                           |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/graph-16.svg" width="16" alt=""/> Monitoring            | PSI + Evidently + Prometheus + Grafana                                               |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/check-circle-16.svg" width="16" alt=""/> Quality        | 107 automated tests · CI                                                             |

The current deployment uses a lightweight Render setup; Kubernetes/K3s and Terraform are documented as the scale-up path.

[Repository](https://github.com/Sow221/cif-credit-intelligencedescription) · [Live API](https://cif-credit-intelligence.onrender.com/docs)

> The live API runs on a free tier; the first request may take a moment to wake the service.

---

### CIF Credit Platform

**Decision-support application**

An application layer for explainable and auditable lending decisions.

| Area                                                                                                                          | Implementation                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/git-branch-16.svg" width="16" alt=""/> Decision engine | Four-way decision workflow: approval, human review, adjustment, refusal                   |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/cpu-16.svg" width="16" alt=""/> Risk modelling         | XGBoost probability of default + isotonic calibration                                     |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/search-16.svg" width="16" alt=""/> Explainability      | SHAP local and global explanations                                                        |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/cash-16.svg" width="16" alt=""/> Decision policy       | Cost-driven thresholds and human-review capacity                                          |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/shield-check-16.svg" width="16" alt=""/> Governance    | Temporal validation, bootstrap confidence intervals, segment analysis and fairness checks |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/database-16.svg" width="16" alt=""/> Traceability      | Model registry, experiment journal and audit-oriented architecture                        |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/git-branch-16.svg" width="16" alt=""/> Reproducibility | DVC pipeline + automated tests + documented validation protocol                           |

The reported performance figures are experimental results on synthetic data; they are **not presented as CIF production performance**.

[Repository](https://github.com/Sow221/cif-credit-intelligence)

---

### TontineSN

**Private · Fintech application for Senegal**

A Laravel-based application designed around tontine operations and mobile-money workflows.

| Area                                                                                                                            | Implementation                                  |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/workflow-16.svg" width="16" alt=""/> Operations          | Cycles, draws and member roles                  |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/cash-16.svg" width="16" alt=""/> Payments                | Mobile-money payment workflows, QR and webhooks |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/comment-discussion-16.svg" width="16" alt=""/> Messaging | WhatsApp notification workflows                 |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/graph-16.svg" width="16" alt=""/> Data                   | Financial and credit-oriented data processing   |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/check-circle-16.svg" width="16" alt=""/> Engineering     | PHPUnit · PHPStan · CI                          |

**Private repository — code available on request.**

---

<p align="center">
  <img src="https://raw.githubusercontent.com/Sow221/Sow221/main/assets/divider.svg" width="100%" alt=""/>
</p>

## 02 · Architecture

```mermaid
flowchart LR
    A[Credit data] --> B[DVC + Dagster]
    B --> C[XGBoost + MLflow]
    C --> D[FastAPI scoring API]
    D --> E[Decision engine]
    E --> F[React / TypeScript interface]

    D --> G[Monitoring]
    G --> H[Evidently]
    G --> I[Prometheus]
    G --> J[Grafana]

    subgraph CIF_ENGINE["CIF Credit Engine"]
        B
        C
        D
        G
    end

    subgraph CIF_PLATFORM["CIF Credit Platform"]
        E
        F
    end
```

<p align="center">
  <img src="https://raw.githubusercontent.com/Sow221/Sow221/main/assets/divider.svg" width="100%" alt=""/>
</p>

## 03 · Tech stack

| Layer              | Technologies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Languages          | <img src="https://cdn.simpleicons.org/python" width="18" alt="Python"/> Python · <img src="https://cdn.simpleicons.org/typescript" width="18" alt="TypeScript"/> TypeScript · <img src="https://cdn.simpleicons.org/javascript" width="18" alt="JavaScript"/> JavaScript · <img src="https://cdn.simpleicons.org/php" width="18" alt="PHP"/> PHP · <img src="https://cdn.simpleicons.org/openjdk" width="18" alt="Java"/> Java                                                                                                                                  |
| Backend / frontend | <img src="https://cdn.simpleicons.org/fastapi" width="18" alt="FastAPI"/> FastAPI · <img src="https://cdn.simpleicons.org/laravel" width="18" alt="Laravel"/> Laravel · <img src="https://cdn.simpleicons.org/react" width="18" alt="React"/> React · <img src="https://cdn.simpleicons.org/nextdotjs" width="18" alt="Next.js"/> Next.js · <img src="https://cdn.simpleicons.org/vite" width="18" alt="Vite"/> Vite · <img src="https://cdn.simpleicons.org/tailwindcss" width="18" alt="Tailwind CSS"/> Tailwind                                              |
| Data / ML          | <img src="https://cdn.simpleicons.org/scikitlearn" width="18" alt="scikit-learn"/> scikit-learn · <img src="https://cdn.simpleicons.org/tensorflow" width="18" alt="TensorFlow"/> TensorFlow · <img src="https://cdn.simpleicons.org/postgresql" width="18" alt="PostgreSQL"/> PostgreSQL · <img src="https://cdn.simpleicons.org/mysql" width="18" alt="MySQL"/> MySQL · <img src="https://cdn.simpleicons.org/redis" width="18" alt="Redis"/> Redis · pandas · NumPy · XGBoost · SHAP                                                                         |
| MLOps / DevOps     | <img src="https://cdn.simpleicons.org/docker" width="18" alt="Docker"/> Docker · <img src="https://cdn.simpleicons.org/githubactions" width="18" alt="GitHub Actions"/> GitHub Actions · <img src="https://cdn.simpleicons.org/git" width="18" alt="Git"/> Git · <img src="https://cdn.simpleicons.org/linux" width="18" alt="Linux"/> Linux · <img src="https://cdn.simpleicons.org/prometheus" width="18" alt="Prometheus"/> Prometheus · <img src="https://cdn.simpleicons.org/grafana" width="18" alt="Grafana"/> Grafana · MLflow · DVC · Dagster · pytest |

<p align="center">
  <img src="https://raw.githubusercontent.com/Sow221/Sow221/main/assets/divider.svg" width="100%" alt=""/>
</p>

## 04 · Information systems

| Workflow modelling                                    | Audit & traceability                              |
| ----------------------------------------------------- | ------------------------------------------------- |
| Tontine cycles, credit decisions, human-review queues | Append-only audit logs, versioned data and models |

| Access control                                  | Integration                                     |
| ----------------------------------------------- | ----------------------------------------------- |
| JWT, OTP, role-based permissions, multi-tenancy | Mobile-money payments, messaging APIs, webhooks |

<p align="center">
  <img src="https://raw.githubusercontent.com/Sow221/Sow221/main/assets/divider.svg" width="100%" alt=""/>
</p>

## 05 · Currently

|                                                                                                                                  |                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/workflow-16.svg" width="16" alt=""/> **Building**         | CIF: moving from synthetic to real-data validation   |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/mortar-board-16.svg" width="16" alt=""/> **Deepening**    | Software architecture · ML engineering               |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/comment-discussion-16.svg" width="16" alt=""/> **Ask me** | Credit scoring · MLOps · Laravel · FastAPI           |
| <img src="https://raw.githubusercontent.com/primer/octicons/main/icons/briefcase-16.svg" width="16" alt=""/> **Open to**         | Internships · junior software / ML engineering roles |

<p align="center">
  <img src="https://raw.githubusercontent.com/Sow221/Sow221/main/assets/footer-wave.svg" width="100%" alt=""/>
</p>

<p align="center">
  <a href="https://portefolio-ms.vercel.app">Portfolio</a>
  &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/ms-officiel/">LinkedIn</a>
</p>
