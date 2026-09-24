<a href="https://portefolio-ms.vercel.app">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg"/>
  <img src="assets/banner-light.svg" alt="Moussa Sow — Software Engineering · Information Systems · Data &amp; AI" width="100%"/>
</picture>
</a>

<div align="center">

<a href="https://portefolio-ms.vercel.app"><img src="https://img.shields.io/badge/Portfolio-0D1117?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"/></a>
<a href="https://www.linkedin.com/in/ms-officiel"><img src="https://img.shields.io/badge/LinkedIn-0D1117?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHJlY3Qgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiByeD0iNCIgZmlsbD0iIzBBNjZDMiIvPjxjaXJjbGUgY3g9IjcuMiIgY3k9IjciIHI9IjEuNyIgZmlsbD0iI2ZmZiIvPjxyZWN0IHg9IjUuNyIgeT0iOS42IiB3aWR0aD0iMyIgaGVpZ2h0PSI4LjkiIGZpbGw9IiNmZmYiLz48cGF0aCBmaWxsPSIjZmZmIiBkPSJNMTAuNiA5LjZoMi45djEuM2MuNS0uOSAxLjYtMS42IDMuMS0xLjYgMi42IDAgMy4zIDEuNyAzLjMgNC4ydjVoLTN2LTQuNGMwLTEuMS0uMi0yLjEtMS40LTIuMS0xLjMgMC0xLjkuOS0xLjkgMi4ydjQuM2gtM3oiLz48L3N2Zz4%3D" alt="LinkedIn"/></a>
<a href="https://cif-credit-intelligence.onrender.com/docs"><img src="https://img.shields.io/badge/Live_API_docs-0D1117?style=for-the-badge&logo=fastapi&logoColor=009688" alt="Live API docs"/></a>
<br/>
<img src="https://img.shields.io/badge/status-open_to_opportunities-14B8A6?style=flat-square&labelColor=0D1117" alt="Status: open to opportunities"/>
<img src="https://img.shields.io/badge/Dakar,_Senegal-0D1117?style=flat-square" alt="Dakar, Senegal"/>

</div>

<br/>

## 01 · Selected work

<table>
<tr>
<td width="44%" valign="top"><img src="assets/card-engine.svg" alt="CIF Credit Engine — data pipelines, model, serving and drift monitoring" width="100%"/></td>
<td valign="top">

### [CIF Credit Engine](https://github.com/Sow221/cif-credit-intelligencedescription)
<samp>credit-risk ML system · open source</samp>

Credit-risk engineering platform for microfinance — built as a **reproducible ML system**, not a notebook.

- Data pipelines versioned with **DVC**, orchestrated with **Dagster**
- **XGBoost** model tracked in **MLflow**, documented with model cards
- Validated on **real Lending Club data**, with a **24-month** monitoring replay
- **FastAPI** serving: JWT, Redis rate limiting, PostgreSQL audit trail
- Drift alerts with a from-scratch **PSI**, Evidently, Prometheus, Grafana
- **125 tests** · CI builds and Trivy-scans the Docker image

<img src="https://img.shields.io/badge/Python-0D1117?style=flat-square&logo=python&logoColor=3776AB" alt="Python"/>
<img src="https://img.shields.io/badge/XGBoost-0D1117?style=flat-square" alt="XGBoost"/>
<img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=009688" alt="FastAPI"/>
<img src="https://img.shields.io/badge/MLflow-0D1117?style=flat-square&logo=mlflow&logoColor=0194E2" alt="MLflow"/>
<img src="https://img.shields.io/badge/DVC-0D1117?style=flat-square&logo=dvc&logoColor=13ADC7" alt="DVC"/>
<img src="https://img.shields.io/badge/Dagster-0D1117?style=flat-square" alt="Dagster"/>

<a href="https://github.com/Sow221/cif-credit-intelligencedescription/actions/workflows/ci.yml"><img src="https://github.com/Sow221/cif-credit-intelligencedescription/actions/workflows/ci.yml/badge.svg" alt="CI status"/></a>
<img src="https://img.shields.io/github/license/Sow221/cif-credit-intelligencedescription?style=flat-square&color=0D1117" alt="License"/>

**[Code →](https://github.com/Sow221/cif-credit-intelligencedescription)** &nbsp; **[Live API docs →](https://cif-credit-intelligence.onrender.com/docs)**

</td>
</tr>
</table>

<table>
<tr>
<td width="44%" valign="top"><img src="assets/card-platform.svg" alt="CIF Credit Platform — SHAP contributions and decision outcomes" width="100%"/></td>
<td valign="top">

### [CIF Credit Platform](https://github.com/Sow221/cif-credit-intelligence)
<samp>decision-support application</samp>

Turns risk scores into **explainable, auditable lending decisions** for credit officers.

- Four-way **decision engine**: approve · human review · adjust · reject
- **Cost-driven thresholds** balancing review capacity and error costs
- Per-client **SHAP** explanations exposed through the API
- **RBAC** with 5 roles, multi-tenant JWT, append-only audit log
- Backend: **124 tests · 84 % coverage**, mypy strict
- **React / TypeScript** UI: 26 Storybook stories, 6 Playwright e2e tests

<img src="https://img.shields.io/badge/React-0D1117?style=flat-square&logo=react&logoColor=61DAFB" alt="React"/>
<img src="https://img.shields.io/badge/TypeScript-0D1117?style=flat-square&logo=typescript&logoColor=3178C6" alt="TypeScript"/>
<img src="https://img.shields.io/badge/FastAPI-0D1117?style=flat-square&logo=fastapi&logoColor=009688" alt="FastAPI"/>
<img src="https://img.shields.io/badge/SHAP-0D1117?style=flat-square" alt="SHAP"/>
<img src="https://img.shields.io/badge/Playwright-0D1117?style=flat-square" alt="Playwright"/>
<img src="https://img.shields.io/badge/Storybook-0D1117?style=flat-square&logo=storybook&logoColor=FF4785" alt="Storybook"/>

**[Code →](https://github.com/Sow221/cif-credit-intelligence)**

</td>
</tr>
</table>

<table>
<tr>
<td width="44%" valign="top"><img src="assets/card-tontine.svg" alt="TontineSN — members in a rotating contribution cycle" width="100%"/></td>
<td valign="top">

### TontineSN
<samp>fintech web application</samp> &nbsp; <img src="https://img.shields.io/badge/private_repository-0D1117?style=flat-square&logo=github&logoColor=white" alt="Private repository"/>

Laravel application digitising **tontines** (rotating savings groups) for the Senegalese market.

- Contribution **cycles and draws**, member roles and administration
- **Mobile-money** payments (PayTech, QR codes), receipts, outbound webhooks
- **WhatsApp** notifications and member credit-scoring
- PHPUnit feature tests, **PHPStan** static analysis, CI

<img src="https://img.shields.io/badge/PHP-0D1117?style=flat-square&logo=php&logoColor=777BB4" alt="PHP"/>
<img src="https://img.shields.io/badge/Laravel-0D1117?style=flat-square&logo=laravel&logoColor=FF2D20" alt="Laravel"/>
<img src="https://img.shields.io/badge/MySQL-0D1117?style=flat-square&logo=mysql&logoColor=4479A1" alt="MySQL"/>
<img src="https://img.shields.io/badge/PHPUnit-0D1117?style=flat-square" alt="PHPUnit"/>

<sub>Code available on request.</sub>

</td>
</tr>
</table>

> [!NOTE]
> The live API runs on a free tier — the first request may take about a minute to wake it up.

<img src="assets/divider.svg" width="100%" height="12" alt=""/>

## 02 · Architecture

How the two CIF repositories fit together:

```mermaid
flowchart LR
    D[("Credit data")] -->|versioned| P["DVC + Dagster<br/>pipelines"]
    P -->|features| T["XGBoost<br/>MLflow registry"]
    T -->|model artifact| API["FastAPI<br/>scoring API"]
    API -->|scores + SHAP| DE["Decision engine<br/>approve · review · adjust · reject"]
    DE --> UI["React / TypeScript<br/>decision interface"]
    API -.->|metrics · PSI| M["Monitoring<br/>Evidently · Prometheus · Grafana"]

    subgraph ENGINE["CIF Credit Engine"]
        D
        P
        T
        API
    end
    subgraph PLATFORM["CIF Credit Platform"]
        DE
        UI
    end

    classDef data fill:#0F766E,stroke:#14B8A6,color:#FFFFFF
    classDef ml fill:#4338CA,stroke:#818CF8,color:#FFFFFF
    classDef app fill:#1E293B,stroke:#64748B,color:#FFFFFF
    class D,P data
    class T,API ml
    class DE,UI,M app
    style ENGINE fill:transparent,stroke:#14B8A6,stroke-dasharray:4 4
    style PLATFORM fill:transparent,stroke:#6366F1,stroke-dasharray:4 4
```

<img src="assets/divider.svg" width="100%" height="12" alt=""/>

## 03 · Tech stack

<table>
<tr><td><samp>languages</samp></td><td><picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=py,ts,js,php,java&theme=dark&perline=8"/><img src="https://skillicons.dev/icons?i=py,ts,js,php,java&theme=light&perline=8" alt="Python, TypeScript, JavaScript, PHP, Java" height="44"/></picture></td></tr>
<tr><td><samp>backend · frontend</samp></td><td><picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=fastapi,laravel,react,nextjs,vite,tailwind&theme=dark&perline=8"/><img src="https://skillicons.dev/icons?i=fastapi,laravel,react,nextjs,vite,tailwind&theme=light&perline=8" alt="FastAPI, Laravel, React, Next.js, Vite, Tailwind CSS" height="44"/></picture></td></tr>
<tr><td><samp>data · ml</samp></td><td><picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=sklearn,tensorflow,postgres,mysql,redis&theme=dark&perline=8"/><img src="https://skillicons.dev/icons?i=sklearn,tensorflow,postgres,mysql,redis&theme=light&perline=8" alt="scikit-learn, TensorFlow, PostgreSQL, MySQL, Redis" height="44"/></picture><br/>
<img src="https://img.shields.io/badge/pandas-0D1117?style=flat-square&logo=pandas&logoColor=E70488" alt="pandas"/>
<img src="https://img.shields.io/badge/NumPy-0D1117?style=flat-square&logo=numpy&logoColor=4DABCF" alt="NumPy"/>
<img src="https://img.shields.io/badge/XGBoost-0D1117?style=flat-square" alt="XGBoost"/>
<img src="https://img.shields.io/badge/SHAP-0D1117?style=flat-square" alt="SHAP"/></td></tr>
<tr><td><samp>mlops · devops</samp></td><td><picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=docker,githubactions,git,linux,prometheus,grafana&theme=dark&perline=8"/><img src="https://skillicons.dev/icons?i=docker,githubactions,git,linux,prometheus,grafana&theme=light&perline=8" alt="Docker, GitHub Actions, Git, Linux, Prometheus, Grafana" height="44"/></picture><br/>
<img src="https://img.shields.io/badge/MLflow-0D1117?style=flat-square&logo=mlflow&logoColor=0194E2" alt="MLflow"/>
<img src="https://img.shields.io/badge/DVC-0D1117?style=flat-square&logo=dvc&logoColor=13ADC7" alt="DVC"/>
<img src="https://img.shields.io/badge/Dagster-0D1117?style=flat-square" alt="Dagster"/>
<img src="https://img.shields.io/badge/pytest-0D1117?style=flat-square&logo=pytest&logoColor=0A9EDC" alt="pytest"/></td></tr>
</table>

<img src="assets/divider.svg" width="100%" height="12" alt=""/>

## 04 · Information systems

<table>
<tr>
<td width="50%" valign="top">

**⚙️ Workflow modelling**<br/>
<sub>Tontine cycles, credit decisions, human-review queues</sub>

</td>
<td width="50%" valign="top">

**🔍 Audit & traceability**<br/>
<sub>Append-only audit logs, versioned data and models</sub>

</td>
</tr>
<tr>
<td valign="top">

**🔐 Access control**<br/>
<sub>JWT, OTP, role-based permissions, multi-tenancy</sub>

</td>
<td valign="top">

**🔌 Integration**<br/>
<sub>Mobile-money payments, messaging APIs, webhooks</sub>

</td>
</tr>
</table>

<img src="assets/divider.svg" width="100%" height="12" alt=""/>

## 05 · Currently

<pre>
🔭 building   →  CIF: moving from synthetic to real-data validation
🌱 deepening  →  software architecture · ML engineering
💬 ask me     →  credit scoring · MLOps · Laravel · FastAPI
⚡ open to    →  internships · junior software / ML engineering roles
</pre>

<br/>

<img src="assets/footer-wave.svg" width="100%" height="90" alt=""/>

<div align="center">
<sub>Built with care in Dakar · <a href="https://portefolio-ms.vercel.app">portefolio-ms.vercel.app</a> · <a href="https://www.linkedin.com/in/ms-officiel">LinkedIn</a></sub>
</div>
