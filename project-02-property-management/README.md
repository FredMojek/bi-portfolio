# Project 02 — Property Portfolio Intelligence Suite

## The Problem

Property managers running 15–50 units across multiple properties make critical decisions about rent increases, maintenance spend, and vacancy response based on gut feel and disconnected spreadsheets.

They have rent data in one system, maintenance costs in another, vacancy rates in a spreadsheet, and compliance deadlines buried in email. No single view exists of which properties are performing, which are dragging the portfolio, and what to do about it today.

## The Solution

An end-to-end BI solution built on Microsoft Fabric that delivers diagnostic, predictive, and prescriptive analytics across a property portfolio — answering not just what is happening, but why it's happening, what will happen next, and exactly what action to take.

## Call to Action Framework Applied

| Layer | Question | What We Built |
|---|---|---|
| Diagnostic | Why is this property underperforming? | Root cause analysis — maintenance WO backlog, collection rates, vacancy cost per day |
| Predictive | Which units will go vacant in 30–60 days? | ML vacancy risk score per unit using scikit-learn |
| Prescriptive | What should I do this week? | AI-generated action cards with specific recommended next steps |

## Architecture

```
DATA SOURCES (4 sources)
├── 01_properties.xlsx              5 properties, 80 units, $20.75M portfolio
├── 02_tenants_leases.xlsx          80 tenant records with vacancy risk scores
├── 03_maintenance_work_orders.csv  148 work orders across all properties
└── 04_rent_transactions.json       924 payment records across 12 months
          ↓
MICROSOFT FABRIC LAKEHOUSE (Medallion Architecture)
├── Bronze Layer    Raw ingestion via Gen2 Dataflows + Python
├── Silver Layer    Cleaned, conformed, deduped via PySpark Notebook
└── Gold Layer      Dimensional model ready for Power BI semantic model
          ↓
FABRIC NOTEBOOKS (Python / PySpark)
├── 01_bronze_ingestion.ipynb
├── 02_silver_transform.ipynb
├── 03_gold_model.ipynb
└── 04_vacancy_prediction_model.ipynb    scikit-learn vacancy risk scoring
          ↓
POWER BI SEMANTIC MODEL
├── Optimised star schema
├── DAX measures (diagnostic + predictive KPIs)
├── Row Level Security by property manager
└── Copilot for Power BI enabled (natural language Q&A)
          ↓
GITHUB CI/CD
└── .github/workflows/powerbi_validate.yml
```

## The Stories in the Data

Three deliberate problem narratives embedded in the synthetic dataset:

### Story 1 — Deferred Maintenance (Diagnostic)
**P-004 Millwoods Townhomes** has 27 overdue work orders — nearly 3x any other property. This is the root cause of its underperformance. The dashboard surfaces this as the primary diagnostic insight: deferred maintenance is compounding and driving tenant dissatisfaction.

### Story 2 — Vacancy Risk (Predictive)
**P-001 Units 18 and 22** carry vacancy risk scores of 78/100 based on payment history (late payments in 4 of 12 months) and 4 maintenance complaints each. The ML model flags these as high probability vacancies in the next lease cycle — before the tenant gives notice.

### Story 3 — Revenue Leakage (Prescriptive)
**3 units vacant** across P-003 and P-004, generating $0 revenue. Combined estimated monthly revenue loss: ~$8,400. The prescriptive action card surfaces the specific vacancy marketing steps to take this week.

## Key Metrics Delivered

| Metric | Description |
|---|---|
| Portfolio Occupancy Rate | Occupied units / total units across all properties |
| Net Operating Income (NOI) per Property | Rent collected minus maintenance and operating costs |
| Vacancy Risk Score | ML-generated 0–100 score per unit (scikit-learn) |
| Maintenance Cost per Unit | Total WO cost per unit over trailing 12 months |
| Rent Collection Rate | Payments received on time / total payments due |
| Days Vacant (Revenue Loss) | Vacancy duration × daily rent rate |

## Data Sources

| File | Format | Records | Key Fields |
|---|---|---|---|
| 01_properties.xlsx | Excel | 5 | Property ID, Units, Purchase Price, Current Value |
| 02_tenants_leases.xlsx | Excel | 80 | Lease Status, Monthly Rent, Payment History, Vacancy Risk Score |
| 03_maintenance_work_orders.csv | CSV | 148 | Category, Priority, Status, Cost Actual vs Estimated |
| 04_rent_transactions.json | JSON | 924 | Due Date, Payment Date, Amount Paid, Days Late, Status |

## Technical Stack

| Tool | Purpose |
|---|---|
| Microsoft Fabric Lakehouse | Medallion architecture — Bronze / Silver / Gold |
| Gen2 Dataflows | No-code ingestion from Excel and CSV sources |
| PySpark (Fabric Notebooks) | Silver layer transformation and data quality |
| Python scikit-learn | Vacancy risk prediction model |
| Power BI Semantic Model | Star schema, DAX measures, RLS |
| Copilot for Power BI | Natural language Q&A embedded in dashboard |
| GitHub Actions | CI/CD validation on every commit |

## Fabric Notebook Summary

| Notebook | Layer | Purpose |
|---|---|---|
| 01_bronze_ingestion.ipynb | Bronze | Raw file ingestion, schema validation, load timestamp |
| 02_silver_transform.ipynb | Silver | Null handling, deduplication, data type enforcement, conformed dimensions |
| 03_gold_model.ipynb | Gold | Dimensional model build — fact and dimension tables |
| 04_vacancy_prediction_model.ipynb | Gold | scikit-learn RandomForest vacancy risk scoring |

## Files in This Project

```
project-02-property-management/
├── README.md                          ← This file
├── data/
│   ├── 01_properties.xlsx
│   ├── 02_tenants_leases.xlsx
│   ├── 03_maintenance_work_orders.csv
│   └── 04_rent_transactions.json
├── notebooks/
│   ├── 01_bronze_ingestion.ipynb
│   ├── 02_silver_transform.ipynb
│   ├── 03_gold_model.ipynb
│   └── 04_vacancy_prediction_model.ipynb
├── dax/
│   └── measures.md
└── screenshots/
    └── dashboard.png
```

## Status

> 🔨 **In progress** — Session 2: Fabric Lakehouse medallion architecture and PySpark notebooks
