<div align="center">

# Moussa Sow

**Software Engineering · Information Systems · Data & AI**

I build maintainable, testable, and deployable software systems, APIs, and data-driven platforms<br/>extended with machine learning where it creates real business value.

[🌐 Portfolio](https://portefolio-ms.vercel.app) &nbsp;•&nbsp; [💼 LinkedIn](https://www.linkedin.com/in/ms-officiel) &nbsp;•&nbsp; [⚡ Live API Docs](https://cif-credit-intelligence.onrender.com/docs)

</div>

---

### 📈 GitHub Overview

<div align="center">

![Moussa's GitHub Stats](https://github-readme-stats.vercel.app/api?username=Sow221&show_icons=true&theme=monokai&hide_border=true&count_private=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Sow221&layout=compact&theme=monokai&hide_border=true)

</div>

---

## 🚀 Selected Work

### 💳 [CIF Credit Engine](https://github.com/Sow221/cif-credit-intelligence) &nbsp;·&nbsp; <sub>Credit-risk MLOps Platform</sub>

> Open-source credit-risk engineering platform for microfinance institutions — built as a **reproducible ML system**, not a notebook.

- **Data pipelines** versioned with DVC and orchestrated with Dagster.
- **XGBoost** default-probability model tracked in MLflow, documented with model cards.
- **FastAPI** serving with JWT auth, rate limiting, and a PostgreSQL audit trail.
- **Monitoring** of data drift with Evidently, Prometheus, and Grafana; CI builds and Trivy-scans the Docker image.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189FDD?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-13ADC7?style=flat-square&logo=dvc&logoColor=white)
![Dagster](https://img.shields.io/badge/Dagster-4F43DD?style=flat-square)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

👉 **[Repository](https://github.com/Sow221/cif-credit-intelligence)** · **[Live API Docs](https://cif-credit-intelligence.onrender.com/docs)** <sub>(Free tier — first request may take a minute)</sub>

---

### 📊 [CIF Credit Platform](https://github.com/Sow221/cif-credit-intelligence) &nbsp;·&nbsp; <sub>Decision-Support Application</sub>

> Decision-support application for credit officers, turning risk scores into **explainable, auditable lending decisions**.

- **Calibrated scoring** — XGBoost on 25 features, recalibrated with isotonic regression.
- **Decision engine** with four outcomes: *approve* · *human review* · *adjust* · *reject*.
- **Explainability** — per-client SHAP contributions exposed through the API.
- **Cost-driven thresholds** balancing review capacity, false positives, and false negatives.
- **React / TypeScript** interface, end-to-end tested with Playwright and documented in Storybook.

![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-FF0051?style=flat-square)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square)
![Storybook](https://img.shields.io/badge/Storybook-FF4785?style=flat-square&logo=storybook&logoColor=white)

---

### 🔐 TontineSN &nbsp;·&nbsp; <sub>Private Repository — Code available upon request</sub>

> Enterprise Laravel application digitising tontines (rotating savings groups) tailored for the Senegalese market.

- **Contribution cycles and draws**, member roles, and automated governance.
- **Mobile-money integration** (PayTech, QR codes), digital receipts, and outbound webhooks.
- **WhatsApp notifications** and automated credit-scoring model for members.
- **Quality Assurance** — PHPUnit feature tests, PHPStan static analysis, and GitHub Actions CI.

![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white)
![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![PHPUnit](https://img.shields.io/badge/PHPUnit-3C9CD7?style=flat-square)

---

## 🏗️ How the CIF System Fits Together

```mermaid
flowchart LR
    subgraph ENGINE["CIF Credit Engine (Data & MLOps)"]
        direction TB
        D[("Credit Data")] --> P["DVC + Dagster Pipelines"]
        P --> T["XGBoost Training & MLflow Registry"]
    end

    T --> API["FastAPI Scoring & Decision API"]
    API --> M["Monitoring: Evidently · Prometheus · Grafana"]

    subgraph PLATFORM["CIF Credit Platform (Decision UI)"]
        direction TB
        DE["Decision Engine<br/>Approve · Review · Adjust · Reject"] --> UI["React / TS UI<br/>SHAP Explanations"]
    end

    API --> DE
