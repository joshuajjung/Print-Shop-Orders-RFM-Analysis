# Customer Segmentation with RFM Analysis (Print Shop)

This project uses RFM (Recency, Frequency, Monetary) analysis to segment customers of a fictitious digital print shop and answer key marketing questions such as **who are the best customers, who needs a retention campaign, and which segments are safe to ignore**.

## Project Overview

The dataset simulates orders for a small online print shop selling various types of digital prints. Each order includes:

- Customer ID
- Order date
- Quantity
- Unit price
- Order value (quantity × unit price)

Using this transactional data, I aggregate at the customer level and apply RFM analysis to understand customer behavior and value.

## RFM Methodology

For each customer, I calculate:

- **Recency (R)** – Days since the customer’s most recent order (lower = better).
- **Frequency (F)** – Number of orders placed by the customer.
- **Monetary (M)** – Total revenue from that customer.

### RFM Scoring (1–5)

I assign R, F, and M scores from 1 to 5 using percentile‑based thresholds in Excel.

Assuming customer‑level metrics are in:

- `B` = Recency
- `C` = Frequency
- `D` = Monetary

I compute scores with `IFS` and `PERCENTILE.INC`:

**Recency score (R) – lower recency is better**

```excel
=IFS(
  B2 <= PERCENTILE.INC($B$2:$B$294,0.2), 5,
  B2 <= PERCENTILE.INC($B$2:$B$294,0.4), 4,
  B2 <= PERCENTILE.INC($B$2:$B$294,0.6), 3,
  B2 <= PERCENTILE.INC($B$2:$B$294,0.8), 2,
  TRUE, 1
)
```

**Frequency score (F) – higher frequency is better**

```excel
=IFS(
  C2 >= PERCENTILE.INC($C$2:$C$294,0.8), 5,
  C2 >= PERCENTILE.INC($C$2:$C$294,0.6), 4,
  C2 >= PERCENTILE.INC($C$2:$C$294,0.4), 3,
  C2 >= PERCENTILE.INC($C$2:$C$294,0.2), 2,
  TRUE, 1
)
```

**Monetary score (M) – higher revenue is better**

```excel
=IFS(
  D2 >= PERCENTILE.INC($D$2:$D$294,0.8), 5,
  D2 >= PERCENTILE.INC($D$2:$D$294,0.6), 4,
  D2 >= PERCENTILE.INC($D$2:$D$294,0.4), 3,
  D2 >= PERCENTILE.INC($D$2:$D$294,0.2), 2,
  TRUE, 1
)
```

RFM Total Score and Segments
I compute an overall RFM total as:

```excel
=E2 + F2 + G2
```

(where E, F, G hold R, F, M scores) and then map the total to segments:

```excel
=IFS(
  H2 >= 13, "Best Customers",
  H2 >= 10, "Loyal Customers",
  H2 >= 7,  "Potential Loyal Customers",
  H2 >= 4,  "Needs Attention",
  TRUE,     "At Risk"
)
```

This yields five intuitive segments based on overall engagement and value.

## Analysis & Outputs
Using PivotTables in Excel, I summarize:

Count of customers by RFM segment

**Results:**

- 69 Best Customers

- 50 Needs Attention

- 17 At Risk

(Remaining customers fall into Loyal / Potential Loyal segments)

These segments are then used to answer three **business questions**:

**Who are my best customers?**

Customers with RFM total ≥ 13 (Best Customers segment).

**Who needs a retention campaign?**

Primarily customers in the Needs Attention segments.

**Which segments are safe to ignore?**

Lower‑value segments (e.g., low RFM total scoring as At Risk with very low F and M) can be deprioritized or only included in low‑touch campaigns, while focus remains on Best, Loyal, and Potential Loyal segments.

## Tools & Skills
Python – for synthetic order data generation (print‑shop orders).

Excel – for:

- Customer‑level aggregation

- R/F/M calculation

- Percentile‑based scoring with IFS + PERCENTILE.INC

- PivotTables and segment summaries

Analytics Concepts

- RFM analysis

- Customer segmentation

- Retention and loyalty strategy thinking

<img width="578" height="410" alt="RFM Pivot" src="https://github.com/user-attachments/assets/810e368b-0d32-4aa1-a2be-4b3fbf2e8dbd" />
