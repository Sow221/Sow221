<div align="center">

# Moussa Sow

### Software Engineering · Information Systems · Data & AI

I build software systems and digital products — applications, APIs and data-driven systems<br/>
that are **maintainable, testable and deployable**, extended with machine learning where it creates real value.

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://portefolio-ms.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logoColor=white)](https://www.linkedin.com/in/ms-officiel)
[![Live API](https://img.shields.io/badge/Live_API_docs-46E3B7?style=for-the-badge&logo=render&logoColor=black)](https://cif-credit-intelligence.onrender.com/docs)

</div>

---

##  Selected work

### [CIF Credit Engine](https://github.com/Sow221/cif-credit-intelligencedescription) &nbsp;·&nbsp; <sub>credit-risk ML system</sub>

> Open-source credit-risk engineering platform for microfinance institutions — built as a **reproducible ML system**, not a notebook.

- **Data pipelines** versioned with DVC and orchestrated with Dagster
- **XGBoost** default-probability model tracked in MLflow, documented with model cards
- **FastAPI** serving with JWT auth, rate limiting and a PostgreSQL audit trail
- **Monitoring** of data drift with Evidently, Prometheus and Grafana; CI builds and Trivy-scans the Docker image

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189FDD?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-13ADC7?style=flat-square&logo=dvc&logoColor=white)
![Dagster](https://img.shields.io/badge/Dagster-4F43DD?style=flat-square)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

**[Code](https://github.com/Sow221/cif-credit-intelligencedescription)** · **[Live API docs](https://cif-credit-intelligence.onrender.com/docs)** <sub>(free tier — first request may take a minute)</sub>

### [CIF Credit Platform](https://github.com/Sow221/cif-credit-intelligence) &nbsp;·&nbsp; <sub>decision-support application</sub>

> Decision-support application for credit officers, turning risk scores into **explainable, auditable lending decisions**.

- **Calibrated scoring** — XGBoost on 25 features, recalibrated with isotonic regression
- **Decision engine** with four outcomes: approve · human review · adjust · reject
- **Explainability** — per-client SHAP contributions exposed through the API
- **Cost-driven thresholds** balancing review capacity, false positives and false negatives
- **React / TypeScript** interface, end-to-end tested with Playwright and documented in Storybook

![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-FF0051?style=flat-square)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square)
![Storybook](https://img.shields.io/badge/Storybook-FF4785?style=flat-square&logo=storybook&logoColor=white)

### TontineSN &nbsp;·&nbsp; <sub>🔒 private repository — code available on request</sub>

> Laravel application digitising tontines (rotating savings groups) for the Senegalese market.

- **Contribution cycles and draws**, member roles and administration
- **Mobile-money payments** (PayTech, QR codes), receipts and outbound webhooks
- **WhatsApp notifications** and credit-scoring of members
- **Quality** — PHPUnit feature tests, PHPStan static analysis, CI with GitHub Actions

![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white)
![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![PHPUnit](https://img.shields.io/badge/PHPUnit-3C9CD7?style=flat-square)

---

##  How the CIF system fits together

```mermaid
flowchart LR
    subgraph ENGINE["CIF Credit Engine — data & MLOps"]
        direction TB
        D[("Credit data")] --> P["DVC + Dagster<br/>pipelines"]
        P --> T["XGBoost training<br/>MLflow registry"]
    end

    T --> API["FastAPI<br/>scoring & decision API"]
    API --> M["Monitoring<br/>Evidently · Prometheus · Grafana"]

    subgraph PLATFORM["CIF Credit Platform — decision interface"]
        direction TB
        DE["Decision engine<br/>approve · review · adjust · reject"] --> UI["React / TypeScript UI<br/>SHAP explanations"]
    end

    API --> DE
```

---

## 🛠️ Tech stack

| Domain | Technologies |
| :--- | :--- |
| **Languages** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white) ![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white) |
| **Backend** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white) ![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white) |
| **Frontend** | ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) ![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white) ![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white) |
| **Data & ML** | ![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white) ![XGBoost](https://img.shields.io/badge/XGBoost-189FDD?style=for-the-badge) ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white) |
| **MLOps** | ![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white) ![DVC](https://img.shields.io/badge/DVC-13ADC7?style=for-the-badge&logo=dvc&logoColor=white) ![Dagster](https://img.shields.io/badge/Dagster-4F43DD?style=for-the-badge) ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white) |
| **Databases** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) |
| **DevOps & quality** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white) |

---

## 🏛️ Information systems

- **Business workflow modelling** — tontine cycles, credit decisions, human-review queues
- **Audit & traceability** — audit trails, versioned models and data, decision logs
- **Access control** — authentication, JWT, role-based permissions
- **Integration** — mobile-money payments, messaging APIs, webhooks

---

## 📌 Currently

Deepening software architecture, information systems and machine learning engineering — building reliable software systems where data and AI create useful capabilities.
