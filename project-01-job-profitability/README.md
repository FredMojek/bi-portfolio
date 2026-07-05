# Project 01 — Job Profitability Dashboard

## The Problem

Trades business owners running 5–10 concurrent jobs have no real-time visibility into which jobs are profitable and which are quietly bleeding margin. By the time they find out, the job is done and the damage is permanent.

A typical contractor knows their total revenue. They rarely know which of their 6 active jobs is actually making money — and which one is silently destroying their margin while it's still running.

## The Solution

A real-time Job Profitability Dashboard built on Power BI and Azure Data Factory that surfaces labour burn rate, cost variance, and cash flow risk across all active jobs simultaneously.

## Call to Action Framework Applied

| Layer | Question | What We Built |
|---|---|---|
| Descriptive | What is the current state of the portfolio? | KPI cards — total contract value, margin %, active jobs, jobs at risk |
| Diagnostic | Which job is over budget and why? | Labour burn rate % per job with At Risk / Watch / Healthy flags |
| Monitoring | What needs attention right now? | Overdue invoice callout with dynamic day counter |
| Prescriptive | What should I do today? | At Risk flag surfaces the specific job needing intervention |

## Architecture

```
Excel (Job Costing Data — 4 sheets)
          ↓
Azure Data Factory (Ingestion Pipeline)
          ↓
Power BI Semantic Model (DAX Measures)
          ↓
Power BI Dashboard (4 visual sections)
```

## Dashboard Screenshot

![Job Profitability Dashboard](screenshots/dashboard.png)

## Key Insights Delivered

| Finding | Metric | Action Triggered |
|---|---|---|
| Sherwood Park Kitchen Reno over budget | 31.8% labour burn rate — At Risk | Immediate crew and cost review |
| Glenmore Office Buildout trending over | 8.8% labour burn rate — Watch | Monitor weekly, pre-empt escalation |
| $28,000 invoice overdue on Glenmore | 14+ days past due | Initiate payment follow-up today |
| Portfolio margin health | 25% across $284,000 in contracts | Baseline established for benchmarking |

## Data Sources

| Sheet | Description | Key Fields |
|---|---|---|
| Projects | Master job list | Job ID, Contract Value, Est. Cost, Status |
| Actuals_WeeklyCosts | Week-by-week labour and materials | Labour Hrs Actual vs Budgeted, Materials Cost |
| Billing_CashFlow | Invoice milestones and payment status | Due Date, Payment Date, Status |
| Summary | Auto-calculated portfolio rollup | Burn Rate, Cost Variance, Margin Health |

## DAX Measures

All measures documented with explanations: [dax/measures.md](dax/measures.md)

**Key measures built:**
- `Labour Burn Rate %` — leading indicator, catches problems before job closes
- `Margin Health` — SWITCH-based traffic light flag (At Risk / Watch / Healthy)
- `Margin Health Color` — hex color code for Power BI conditional formatting
- `Days Overdue Calc` — dynamic calculation from TODAY(), updates automatically
- `Overdue Callout Text` — human-readable sentence combining amount and days

## Technical Stack

| Tool | Purpose |
|---|---|
| Power BI Desktop | Dashboard development and DAX authoring |
| Azure Data Factory | Data ingestion pipeline |
| DAX | Measure calculation and conditional logic |
| Excel (openpyxl) | Synthetic dataset generation |
| Power BI Service | Publishing and sharing |

## Files in This Project

```
project-01-job-profitability/
├── README.md                    ← This file
├── dax/
│   └── measures.md              ← All DAX measures documented
├── data/
│   └── job_profitability_data.xlsx
└── screenshots/
    └── dashboard.png
```

## Synthetic Data Design

The dataset was deliberately constructed with problem stories embedded:

- **J-102 Sherwood Park Kitchen Reno** — Plumbing rework caused 105 hours of overtime labour above budget (31.8% burn rate). Three consecutive weeks of cost escalation visible in the trend chart.
- **J-105 Glenmore Office Buildout** — Phase 1 invoice ($28,000) 14+ days past due. Cash flow risk hidden inside an otherwise healthy-looking portfolio.
- **J-103 Westbrook Plaza Roof Repair** — Materials price spike on steel vs original quote. Absorbed within margin but visible as a Watch signal.

This approach ensures the dashboard demonstrates diagnostic and prescriptive value — not just reporting.
