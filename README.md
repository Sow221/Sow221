<div align="center">

# Moussa Sow

### Software Engineering · Information Systems · Data & AI

I build software systems and digital products — applications, APIs and data-driven systems<br/>
that are **maintainable, testable and deployable**, extended with machine learning where it creates real value.

<br/>

[![Portfolio](PORTFOLIO_URL)](PORTFOLIO_URL)  
[![LinkedIn](LINKEDIN_URL)](LINKEDIN_URL)

<br/>

[![Live API](LIVE_API_URL)](LIVE_API_URL)

</div>

---

## Selected work

### CIF Credit Engine

<sub>Credit-risk ML system · Python · FastAPI · XGBoost · MLflow · DVC · Dagster</sub>

> Open-source credit-risk engineering platform for microfinance institutions — built as a **reproducible ML system**, not a notebook.

* **Data pipelines** — versioned with DVC and orchestrated with Dagster
* **Machine learning** — XGBoost default-probability model tracked in MLflow and documented with model cards
* **API serving** — FastAPI with JWT authentication, rate limiting and a PostgreSQL audit trail
* **Monitoring** — data drift with Evidently, Prometheus and Grafana
* **Engineering** — CI builds and Trivy-scans the Docker image

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white) 
![XGBoost](https://img.shields.io/badge/XGBoost-189FDD?style=flat-square) 
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square\&logo=fastapi\&logoColor=white) 
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square\&logo=mlflow\&logoColor=white) 
![DVC](https://img.shields.io/badge/DVC-13ADC7?style=flat-square\&logo=dvc\&logoColor=white) 
![Dagster](https://img.shields.io/badge/Dagster-4F43DD?style=flat-square) 
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square\&logo=postgresql\&logoColor=white) 
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square\&logo=docker\&logoColor=white)

<br/>

**[Code](ENGINE_REPO_URL)** · **[Live API docs](LIVE_API_URL)** <sub>Free tier — first request may take a minute</sub>

---

### CIF Credit Platform

<sub>Decision-support application · React · TypeScript · FastAPI · SHAP · Playwright · Storybook</sub>

> Decision-support application for credit officers, turning risk scores into **explainable, auditable lending decisions**.

* **Calibrated scoring** — XGBoost on 25 features, recalibrated with isotonic regression
* **Decision engine** — four outcomes: approve · human review · adjust · reject
* **Explainability** — per-client SHAP contributions exposed through the API
* **Cost-driven thresholds** — balancing review capacity, false positives and false negatives
* **Application layer** — React / TypeScript interface integrated with machine-learning services
* **Quality** — end-to-end testing with Playwright and component documentation with Storybook

<br/>

![React](https://img.shields.io/badge/React-20232A?style=flat-square\&logo=react\&logoColor=61DAFB) 
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square\&logo=typescript\&logoColor=white) 
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square\&logo=fastapi\&logoColor=white) 
![SHAP](https://img.shields.io/badge/SHAP-FF0051?style=flat-square) 
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square) 
![Storybook](https://img.shields.io/badge/Storybook-FF4785?style=flat-square\&logo=storybook\&logoColor=white)

<br/>

**[Code](PLATFORM_REPO_URL)**

---

## How the CIF system fits together

```mermaid
flowchart LR

    subgraph ENGINE["CIF Credit Engine — Data & MLOps"]
        direction TB
        D[("Credit data")] --> P["DVC + Dagster<br/>pipelines"]
        P --> T["XGBoost training<br/>MLflow registry"]
    end

    T --> API["FastAPI<br/>scoring & decision API"]

    API --> M["Monitoring<br/>Evidently · Prometheus · Grafana"]

    subgraph PLATFORM["CIF Credit Platform — Decision Interface"]
        direction TB
        DE["Decision engine<br/>approve · review · adjust · reject"]
        DE --> UI["React / TypeScript UI<br/>SHAP explanations"]
    end

    API --> DE
```

---

## Technical stack

### Languages

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white) 
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square\&logo=typescript\&logoColor=white) 
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square\&logo=javascript\&logoColor=black) 
![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat-square\&logo=php\&logoColor=white) 
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square\&logo=openjdk\&logoColor=white)

### Backend & APIs

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square\&logo=fastapi\&logoColor=white) 
![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=flat-square\&logo=laravel\&logoColor=white) 
![REST](https://img.shields.io/badge/REST-005571?style=flat-square)

### Frontend

![React](https://img.shields.io/badge/React-20232A?style=flat-square\&logo=react\&logoColor=61DAFB) 
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square\&logo=nextdotjs\&logoColor=white) 
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square\&logo=vite\&logoColor=white) 
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square\&logo=tailwindcss\&logoColor=white)

### Data & Machine Learning

![Pandas](https://img.shields.io/badge/pandas-150458?style=flat-square\&logo=pandas\&logoColor=white) 
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square\&logo=numpy\&logoColor=white) 
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square\&logo=scikitlearn\&logoColor=white) 
![XGBoost](https://img.shields.io/badge/XGBoost-189FDD?style=flat-square) 
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square\&logo=tensorflow\&logoColor=white)

### MLOps & Observability

![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square\&logo=mlflow\&logoColor=white) 
![DVC](https://img.shields.io/badge/DVC-13ADC7?style=flat-square\&logo=dvc\&logoColor=white) 
![Dagster](https://img.shields.io/badge/Dagster-4F43DD?style=flat-square) 
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square\&logo=prometheus\&logoColor=white) 
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square\&logo=grafana\&logoColor=white)

### Databases

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square\&logo=postgresql\&logoColor=white) 
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square\&logo=mysql\&logoColor=white)

### Engineering & Infrastructure

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square\&logo=docker\&logoColor=white) 
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square\&logo=githubactions\&logoColor=white) 
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square\&logo=git\&logoColor=white) 
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square\&logo=linux\&logoColor=black) 
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square\&logo=pytest\&logoColor=white)

---

## Information systems

* **Business workflows** — modelling operational processes, decision flows and human-review workflows
* **System integration** — REST APIs, external services, webhooks and application-to-service communication
* **Data & traceability** — versioned data, model lifecycle, audit trails and decision logs
* **Security & access control** — authentication, authorization and role-based permissions
* **Deployment** — containerized services, CI/CD and production-oriented engineering practices

---

## Currently

Deepening software architecture, information systems and machine learning engineering — building reliable software systems where **data and AI create useful capabilities**.
