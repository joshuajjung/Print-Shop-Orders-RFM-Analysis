import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# For reproducibility
np.random.seed(42)
random.seed(42)

# Number of order rows
n_rows = 1200  # you can change this if you want more/less

# ---- Core RFM fields you’ll use later ----
# customer_id, order_date, order_value are the essentials

# Create customer IDs (around 300 unique customers)
customer_ids = [f"CUST_{i:04d}" for i in np.random.randint(1, 301, size=n_rows)]

# Define product types for the print shop
product_types = [
    "Minimalist poster",
    "Abstract canvas",
    "Photo collage",
    "Typography print",
    "Line art print",
    "Nature landscape",
    "Cityscape print",
    "Vintage poster"
]

# Unique order IDs
order_ids = [f"ORD_{i:06d}" for i in range(1, n_rows + 1)]

# Order dates over the last 12 months
end_date = datetime(2026, 1, 25)        # pretend "today" for recency
start_date = end_date - timedelta(days=365)
order_dates = [
    start_date + timedelta(days=int(x))
    for x in np.random.randint(0, 366, size=n_rows)
]

# Quantities per order (1–5 prints)
quantities = np.random.randint(1, 6, size=n_rows)

# Unit prices (skewed toward cheaper prints)
unit_prices = np.random.choice(
    [9.99, 14.99, 19.99, 24.99, 29.99, 39.99, 49.99],
    size=n_rows,
    p=[0.2, 0.2, 0.2, 0.15, 0.1, 0.1, 0.05]
)

# Monetary value per order
order_values = quantities * unit_prices

# Product type and country per order
product_choices = np.random.choice(product_types, size=n_rows)
countries = np.random.choice(
    ["US", "CA", "UK", "AU", "DE"],
    size=n_rows,
    p=[0.6, 0.1, 0.1, 0.1, 0.1]
)

# Build orders DataFrame
orders_df = pd.DataFrame({
    "order_id": order_ids,
    "customer_id": customer_ids,
    "order_date": order_dates,
    "product_type": product_choices,
    "quantity": quantities,
    "unit_price": unit_prices,
    "order_value": order_values,
    "currency": "USD",
    "country": countries
})

# Save to CSV in your current working directory
filename = "print_shop_orders_rfm_demo.csv"
orders_df.to_csv(filename, index=False)

print(f"Saved {len(orders_df)} rows to {filename}")
print(orders_df.head())
