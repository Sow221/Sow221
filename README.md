<a href="https://portefolio-ms.vercel.app">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg"/>
  <img src="assets/banner-light.svg" alt="Moussa Sow — Software Engineering · Information Systems · Data &amp; AI" width="100%"/>
</picture>
</a>

<br/>

<div align="center">

<h1>Software Engineering · Information Systems · Data &amp; AI</h1>

<p>
Software engineer building digital systems across applications, data and AI.
</p>

<br/>

<a href="https://portefolio-ms.vercel.app"><img src="https://img.shields.io/badge/Portfolio-0D1117?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"/></a> <a href="https://www.linkedin.com/in/ms-officiel"><img src="https://img.shields.io/badge/LinkedIn-0D1117?style=for-the-badge&logo=linkedin&logoColor=0A66C2" alt="LinkedIn"/></a> <a href="https://cif-credit-intelligence.onrender.com/docs"><img src="https://img.shields.io/badge/Live_API_docs-0D1117?style=for-the-badge&logo=fastapi&logoColor=009688" alt="Live API docs"/></a>

<br/><br/>

<img src="https://img.shields.io/badge/Software_Engineering-0D1117?style=flat-square&logo=github&logoColor=white" alt="Software Engineering"/>
<img src="https://img.shields.io/badge/Dakar%2C_Senegal-0D1117?style=flat-square&logo=googlemaps&logoColor=4285F4" alt="Dakar, Senegal"/>

</div>

<br/>

## 01 · Selected work

I build software systems where **applications, data, machine learning and operational workflows** meet — with an emphasis on reproducibility, traceability and integration.

<table>
<tr>
<td width="42%" valign="top">
<img src="assets/card-engine.svg" alt="CIF Credit Engine" width="96%"/>
</td>
<td width="4%"></td>
<td width="54%" valign="top">

### [CIF Credit Engine](https://github.com/Sow221/cif-credit-intelligencedescription)

<samp>credit-risk ML system · open source</samp>

Credit-risk engineering platform for microfinance — built as a **reproducible ML system**, not a notebook.

* Data pipelines versioned with **DVC**, orchestrated with **Dagster**
* **XGBoost** model tracked in **MLflow**, documented with model cards
* Method validated on **public Lending Club data** with an **out-of-time evaluation protocol**
* **FastAPI** serving: JWT, Redis rate limiting, PostgreSQL audit trail
* Drift alerts with a from-scratch **PSI**, Evidently, Prometheus, Grafana
* **107 tests** · 74 % coverage · CI with linting, type checking and Docker image scanning

<br/>

<img src="https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=3776AB" alt="Python"/>
<img src="https://img.shields.io/badge/XGBoost-0D1117?style=flat-square&logo=xgboost&logoColor=4285F4" alt="XGBoost"/>
<img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=009688" alt="FastAPI"/>
<img src="https://img.shields.io/badge/MLflow-0D1117?style=flat-square&logo=mlflow&logoColor=0194E2" alt="MLflow"/>
<img src="https://img.shields.io/badge/DVC-0D1117?style=flat-square&logo=dvc&logoColor=13ADC7" alt="DVC"/>
<img src="https://img.shields.io/badge/Dagster-0D1117?style=flat-square&logo=dagster&logoColor=00AEEF" alt="Dagster"/>

<br/><br/>

<a href="https://github.com/Sow221/cif-credit-intelligencedescription"><img src="https://img.shields.io/badge/Code_%E2%86%92-0D1117?style=for-the-badge&logo=github&logoColor=white" alt="Code"/></a> <a href="https://cif-credit-intelligence.onrender.com/docs"><img src="https://img.shields.io/badge/Live_API_docs_%E2%86%92-0D1117?style=for-the-badge&logo=fastapi&logoColor=009688" alt="Live API docs"/></a>

</td>
</tr>

<tr><td colspan="3"><br/></td></tr>

<tr>
<td width="42%" valign="top">
<img src="assets/card-platform.svg" alt="CIF Credit Platform" width="96%"/>
</td>
<td width="4%"></td>
<td width="54%" valign="top">

### [CIF Credit Platform](https://github.com/Sow221/cif-credit-intelligence)

<samp>decision-support application</samp>

Turns risk scores into **explainable, auditable lending decisions** for credit officers.

* Four-way **decision engine**: approve · human review · adjust · reject
* **Cost-driven thresholds** balancing review capacity and error costs
* Per-client **SHAP** explanations exposed through the API
* **RBAC**, multi-tenant JWT and append-only audit trail
* Temporal validation, anti-leakage controls and segmented evaluation
* CI with **ruff, mypy, pytest and anti-leakage checks**

<br/>

<img src="https://img.shields.io/badge/React-0D1117?style=flat-square&logo=react&logoColor=61DAFB" alt="React"/>
<img src="https://img.shields.io/badge/TypeScript-0D1117?style=flat-square&logo=typescript&logoColor=3178C6" alt="TypeScript"/>
<img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=009688" alt="FastAPI"/>
<img src="https://img.shields.io/badge/SHAP-0D1117?style=flat-square&logoColor=FFFFFF" alt="SHAP"/>
<img src="https://img.shields.io/badge/Playwright-0D1117?style=flat-square&logo=playwright&logoColor=45BA4B" alt="Playwright"/>
<img src="https://img.shields.io/badge/Storybook-0D1117?style=flat-square&logo=storybook&logoColor=FF4785" alt="Storybook"/>

<br/><br/>

<a href="https://github.com/Sow221/cif-credit-intelligence"><img src="https://img.shields.io/badge/Code_%E2%86%92-0D1117?style=for-the-badge&logo=github&logoColor=white" alt="Code"/></a>

</td>
</tr>

<tr><td colspan="3"><br/></td></tr>

<tr>
<td width="42%" valign="top">
<img src="assets/card-tontine.svg" alt="TontineSN" width="96%"/>
</td>
<td width="4%"></td>
<td width="54%" valign="top">

### TontineSN

<samp>fintech web application · private repository</samp>

Laravel application digitising **tontines** (rotating savings groups) for the Senegalese market.

* Contribution **cycles and draws**, member roles and administration
* **Mobile-money** payment integration, QR flows, receipts and outbound webhooks
* **WhatsApp** notifications and member credit-scoring
* PHPUnit feature tests, **PHPStan** static analysis, CI

<br/>

<img src="https://img.shields.io/badge/PHP-0D1117?style=flat-square&logo=php&logoColor=777BB4" alt="PHP"/>
<img src="https://img.shields.io/badge/Laravel-0D1117?style=flat-square&logo=laravel&logoColor=FF2D20" alt="Laravel"/>
<img src="https://img.shields.io/badge/MySQL-0D1117?style=flat-square&logo=mysql&logoColor=4479A1" alt="MySQL"/>
<img src="https://img.shields.io/badge/PHPUnit-0D1117?style=flat-square&logo=phpunit&logoColor=4C9A2A" alt="PHPUnit"/>

<br/><br/>

<sub>Private work · code available on request.</sub>

</td>
</tr>
</table>

<br/>

> [!NOTE]
> The live API runs on a free tier — the first request may take about a minute to wake it up.

<br/>

<img src="assets/divider.svg" width="100%" height="12" alt=""/>

## 02 · Architecture

The two CIF repositories form one engineering chain:

```mermaid
flowchart LR

    D[Credit data]
    P[DVC + Dagster pipelines]
    M[XGBoost + MLflow registry]
    A[FastAPI scoring API]
    E[Decision engine]
    U[Decision interface]
    O[Evidently + Prometheus + Grafana]

    D --> P
    P --> M
    M --> A
    A --> E
    E --> U
    A -.-> O

    subgraph ENGINE["CIF Credit Engine"]
        P
        M
        A
    end

    subgraph PLATFORM["CIF Credit Platform"]
        E
        U
    end

    classDef data fill:#0F766E,stroke:#14B8A6,color:#FFFFFF
    classDef ml fill:#4338CA,stroke:#818CF8,color:#FFFFFF
    classDef app fill:#1E293B,stroke:#64748B,color:#FFFFFF

    class D,P data
    class M ml
    class A,E,U,O app

    style ENGINE fill:transparent,stroke:#14B8A6,stroke-dasharray:5 5
    style PLATFORM fill:transparent,stroke:#6366F1,stroke-dasharray:5 5
```

<br/>

<img src="assets/divider.svg" width="100%" height="12" alt=""/>

## 03 · Tech stack

The stack below reflects technologies used across my public work and broader software engineering practice — not a list of every technology I have ever touched.

<table>
<tr>
<td width="22%" valign="top"><strong>Languages</strong></td>
<td valign="top">
<img src="https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=3776AB" alt="Python"/>
<img src="https://img.shields.io/badge/TypeScript-0D1117?style=flat-square&logo=typescript&logoColor=3178C6" alt="TypeScript"/>
<img src="https://img.shields.io/badge/JavaScript-0D1117?style=flat-square&logo=javascript&logoColor=F7DF1E" alt="JavaScript"/>
<img src="https://img.shields.io/badge/PHP-0D1117?style=flat-square&logo=php&logoColor=777BB4" alt="PHP"/>
<img src="https://img.shields.io/badge/Java-0D1117?style=flat-square&logo=openjdk&logoColor=FFFFFF" alt="Java"/>
</td>
</tr>

<tr>
<td width="22%" valign="top"><strong>Backend · frontend</strong></td>
<td valign="top">
<img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=009688" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Laravel-0D1117?style=flat-square&logo=laravel&logoColor=FF2D20" alt="Laravel"/>
<img src="https://img.shields.io/badge/React-0D1117?style=flat-square&logo=react&logoColor=61DAFB" alt="React"/>
<img src="https://img.shields.io/badge/Next.js-0D1117?style=flat-square&logo=nextdotjs&logoColor=FFFFFF" alt="Next.js"/>
<img src="https://img.shields.io/badge/Vite-0D1117?style=flat-square&logo=vite&logoColor=646CFF" alt="Vite"/>
<img src="https://img.shields.io/badge/Tailwind_CSS-0D1117?style=flat-square&logo=tailwindcss&logoColor=06B6D4" alt="Tailwind CSS"/>
</td>
</tr>

<tr>
<td width="22%" valign="top"><strong>Data · ML</strong></td>
<td valign="top">
<img src="https://img.shields.io/badge/scikit--learn-0D1117?style=flat-square&logo=scikitlearn&logoColor=F7931E" alt="scikit-learn"/>
<img src="https://img.shields.io/badge/TensorFlow-0D1117?style=flat-square&logo=tensorflow&logoColor=FF6F00" alt="TensorFlow"/>
<img src="https://img.shields.io/badge/PostgreSQL-0D1117?style=flat-square&logo=postgresql&logoColor=4169E1" alt="PostgreSQL"/>
<img src="https://img.shields.io/badge/MySQL-0D1117?style=flat-square&logo=mysql&logoColor=4479A1" alt="MySQL"/>
<img src="https://img.shields.io/badge/Redis-0D1117?style=flat-square&logo=redis&logoColor=DC382D" alt="Redis"/>
<br/>
<img src="https://img.shields.io/badge/Pandas-0D1117?style=flat-square&logo=pandas&logoColor=150458" alt="Pandas"/>
<img src="https://img.shields.io/badge/NumPy-0D1117?style=flat-square&logo=numpy&logoColor=013243" alt="NumPy"/>
<img src="https://img.shields.io/badge/XGBoost-0D1117?style=flat-square&logo=xgboost&logoColor=4285F4" alt="XGBoost"/>
<img src="https://img.shields.io/badge/SHAP-0D1117?style=flat-square&logoColor=FFFFFF" alt="SHAP"/>
</td>
</tr>

<tr>
<td width="22%" valign="top"><strong>MLOps · DevOps</strong></td>
<td valign="top">
<img src="https://img.shields.io/badge/Docker-0D1117?style=flat-square&logo=docker&logoColor=2496ED" alt="Docker"/>
<img src="https://img.shields.io/badge/GitHub_Actions-0D1117?style=flat-square&logo=githubactions&logoColor=2088FF" alt="GitHub Actions"/>
<img src="https://img.shields.io/badge/Git-0D1117?style=flat-square&logo=git&logoColor=F05032" alt="Git"/>
<img src="https://img.shields.io/badge/Linux-0D1117?style=flat-square&logo=linux&logoColor=FFFFFF" alt="Linux"/>
<img src="https://img.shields.io/badge/Prometheus-0D1117?style=flat-square&logo=prometheus&logoColor=E6522C" alt="Prometheus"/>
<img src="https://img.shields.io/badge/Grafana-0D1117?style=flat-square&logo=grafana&logoColor=F46800" alt="Grafana"/>
<br/>
<img src="https://img.shields.io/badge/MLflow-0D1117?style=flat-square&logo=mlflow&logoColor=0194E2" alt="MLflow"/>
<img src="https://img.shields.io/badge/DVC-0D1117?style=flat-square&logo=dvc&logoColor=13ADC7" alt="DVC"/>
<img src="https://img.shields.io/badge/Dagster-0D1117?style=flat-square&logo=dagster&logoColor=00AEEF" alt="Dagster"/>
<img src="https://img.shields.io/badge/pytest-0D1117?style=flat-square&logo=pytest&logoColor=0A9EDC" alt="pytest"/>
</td>
</tr>
</table>

<br/>

<img src="assets/divider.svg" width="100%" height="12" alt=""/>

## 04 · Information systems

My work focuses not only on individual applications or models, but on how **people, data, workflows and software systems interact**.

<table cellpadding="12">
<tr>
<td width="7%" align="center" valign="middle">
<img src="https://raw.githubusercontent.com/primer/octicons/main/icons/git-branch-16.svg" width="18" height="18" alt=""/>
</td>
<td width="24%" valign="top"><strong>Workflow modelling</strong></td>
<td valign="top">Tontine cycles, credit decisions, human-review queues</td>
</tr>

<tr>
<td align="center" valign="middle">
<img src="https://raw.githubusercontent.com/primer/octicons/main/icons/search-16.svg" width="18" height="18" alt=""/>
</td>
<td valign="top"><strong>Audit &amp; traceability</strong></td>
<td valign="top">Append-only audit logs, versioned data and models</td>
</tr>

<tr>
<td align="center" valign="middle">
<img src="https://raw.githubusercontent.com/primer/octicons/main/icons/shield-16.svg" width="18" height="18" alt=""/>
</td>
<td valign="top"><strong>Access control</strong></td>
<td valign="top">JWT, OTP, role-based permissions, multi-tenancy</td>
</tr>

<tr>
<td align="center" valign="middle">
<img src="https://raw.githubusercontent.com/primer/octicons/main/icons/plug-16.svg" width="18" height="18" alt=""/>
</td>
<td valign="top"><strong>Integration</strong></td>
<td valign="top">Mobile-money payments, messaging APIs, webhooks</td>
</tr>
</table>

<br/>

<img src="assets/divider.svg" width="100%" height="12" alt=""/>

## 05 · Engineering interests

<table>
<tr>
<td width="25%" valign="top"><strong>Software architecture</strong></td>
<td valign="top">Designing maintainable systems across applications, APIs, data and infrastructure</td>
</tr>

<tr>
<td valign="top"><strong>ML engineering</strong></td>
<td valign="top">Reproducible pipelines, evaluation, serving, monitoring and model governance</td>
</tr>

<tr>
<td valign="top"><strong>Information systems</strong></td>
<td valign="top">Workflow modelling, integration, traceability, access control and digital transformation</td>
</tr>

<tr>
<td valign="top"><strong>Applied AI</strong></td>
<td valign="top">Using machine learning and AI where they create measurable value inside real software systems</td>
</tr>
</table>

<br/>

<img src="assets/divider.svg" width="100%" height="12" alt=""/>

## 06 · Currently

<table>
<tr>
<td width="7%" align="center" valign="middle">
<img src="https://raw.githubusercontent.com/primer/octicons/main/icons/telescope-16.svg" width="18" height="18" alt=""/>
</td>
<td valign="top"><strong>building</strong></td>
<td valign="top">CIF: moving from synthetic to real-data validation</td>
</tr>

<tr>
<td align="center" valign="middle">
<img src="https://raw.githubusercontent.com/primer/octicons/main/icons/mortar-board-16.svg" width="18" height="18" alt=""/>
</td>
<td valign="top"><strong>deepening</strong></td>
<td valign="top">software architecture · ML engineering</td>
</tr>

<tr>
<td align="center" valign="middle">
<img src="https://raw.githubusercontent.com/primer/octicons/main/icons/comment-discussion-16.svg" width="18" height="18" alt=""/>
</td>
<td valign="top"><strong>ask me</strong></td>
<td valign="top">credit scoring · MLOps · Laravel · FastAPI</td>
</tr>

<tr>
<td align="center" valign="middle">
<img src="https://raw.githubusercontent.com/primer/octicons/main/icons/zap-16.svg" width="18" height="18" alt=""/>
</td>
<td valign="top"><strong>open to</strong></td>
<td valign="top">internships · junior software / ML engineering roles</td>
</tr>
</table>

<br/>

<img src="assets/footer-wave.svg" width="100%" alt=""/>

<div align="center">
<sub>Built with care in Dakar · <a href="https://portefolio-ms.vercel.app">portfolio</a> · <a href="https://www.linkedin.com/in/ms-officiel">LinkedIn</a></sub>
</div>
