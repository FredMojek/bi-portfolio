# DAX Measures — Job Profitability Dashboard

## Core Cost Measures

### Total Contract Value
```dax
Total Contract Value = SUM(Projects[Contract Value ($)])
```
Sum of all contract values across the filtered job portfolio.

---

### Total Estimated Cost
```dax
Total Estimated Cost = SUM(Projects[Est. Total Cost ($)])
```
Sum of all estimated costs across the job portfolio.

---

### Total Actual Cost
```dax
Total Actual Cost = SUM(Actuals_WeeklyCosts[Total Weekly Cost ($)])
```
Sum of all actual costs incurred to date across all jobs.

---

### Total Labour Hrs Actual
```dax
Total Labour Hrs Actual = SUM(Actuals_WeeklyCosts[Labour Hrs (Actual)])
```

---

### Total Labour Hrs Budgeted
```dax
Total Labour Hrs Budgeted = SUM(Actuals_WeeklyCosts[Labour Hrs (Budgeted)])
```

---

## Margin Health Measures

### Labour Burn Rate %
```dax
Labour Burn Rate % = 
DIVIDE(
    [Total Labour Hrs Actual] - [Total Labour Hrs Budgeted],
    [Total Labour Hrs Budgeted],
    0
)
```
Percentage by which actual labour hours exceed budgeted hours.
Positive = over budget. Negative = under budget.
This is the leading indicator — it surfaces problems before costs close out.

---

### Margin Health
```dax
Margin Health = 
VAR BurnRate = [Labour Burn Rate %]
RETURN
    SWITCH(
        TRUE(),
        BurnRate > 0.2, "At Risk",
        BurnRate > 0.08, "Watch",
        "Healthy"
    )
```
Traffic light flag based on labour burn rate threshold.
- At Risk: >20% over budgeted hours
- Watch: 8–20% over budgeted hours
- Healthy: <8% over budgeted hours

---

### Margin Health Color
```dax
Margin Health Color = 
VAR BurnRate = [Labour Burn Rate %]
RETURN
    SWITCH(
        TRUE(),
        BurnRate > 0.2, "#C00000",
        BurnRate > 0.08, "#FFC000",
        "#548235"
    )
```
Hex color code for conditional formatting.
Plug into Background Color → Field value in Power BI table visuals.

---

### Cost Variance ($)
```dax
Cost Variance ($) = [Total Actual Cost] - [Total Estimated Cost]
```
Positive = over budget. Negative = under budget.

---

### Cost Variance %
```dax
Cost Variance % = DIVIDE([Cost Variance ($)], [Total Estimated Cost], 0)
```

---

## Portfolio KPI Measures

### Active Jobs Count
```dax
Active Jobs Count = 
CALCULATE(
    DISTINCTCOUNT(Projects[Job ID]),
    Projects[Status] = "In Progress"
)
```

---

### Jobs At Risk
```dax
Jobs At Risk = 
CALCULATE(
    DISTINCTCOUNT(Projects[Job ID]),
    FILTER(
        SUMMARIZE(Actuals_WeeklyCosts, Projects[Job ID]),
        [Labour Burn Rate %] > 0.2
    )
)
```

---

### Total Est. Margin ($)
```dax
Total Est. Margin ($) = SUM(Projects[Est. Margin ($)])
```

---

### Total Est. Margin %
```dax
Total Est. Margin % = DIVIDE([Total Est. Margin ($)], [Total Contract Value], 0)
```

---

## Cash Flow Measures

### Total Outstanding Overdue
```dax
Total Outstanding Overdue = 
CALCULATE(
    SUM(Billing_CashFlow[Invoice Amount ($)]),
    FILTER(
        ALL(Billing_CashFlow),
        SEARCH("past due", Billing_CashFlow[Status], 1, 0) > 0
    )
)
```
Uses ALL() to ignore page-level filter context.
Returns the correct overdue amount regardless of what job is selected.

---

### Days Overdue Calc
```dax
Days Overdue Calc = 
CALCULATE(
    DATEDIFF(MAX(Billing_CashFlow[Due Date]), TODAY(), DAY),
    FILTER(
        ALL(Billing_CashFlow),
        SEARCH("past due", Billing_CashFlow[Status], 1, 0) > 0
    )
)
```
Dynamic calculation from today's date.
Updates automatically every day without manual refresh.

---

### Overdue Invoice Count
```dax
Overdue Invoice Count = 
CALCULATE(
    COUNTROWS(Billing_CashFlow),
    Billing_CashFlow[Status] = "Outstanding",
    Billing_CashFlow[Due Date] < TODAY()
)
```

---

### Overdue Callout Text
```dax
Overdue Callout Text = 
"$" & FORMAT([Total Outstanding Overdue], "#,##0") & 
" invoice " & [Days Overdue Calc] & 
" days overdue — Glenmore Office Buildout"
```
Human-readable sentence for the dashboard callout card.
Combines amount and days into a single actionable statement.
