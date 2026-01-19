import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

# -----------------------------
# Ensure output folder exists
# -----------------------------
os.makedirs("analysis", exist_ok=True)

# -----------------------------
# Connect to SQLite Database
# -----------------------------
conn = sqlite3.connect("pizza_store.db")

# -----------------------------
# Load tables
# -----------------------------
customers = pd.read_sql("SELECT * FROM customers", conn)
orders = pd.read_sql("SELECT * FROM orders", conn)

# -----------------------------
# Normalize column names
# -----------------------------
customers.columns = customers.columns.str.lower().str.replace(" ", "_")
orders.columns = orders.columns.str.lower().str.replace(" ", "_")

# -----------------------------
# Standardize customer_id
# -----------------------------
if "customerid" in customers.columns:
    customers.rename(columns={"customerid": "customer_id"}, inplace=True)

if "customerid" in orders.columns:
    orders.rename(columns={"customerid": "customer_id"}, inplace=True)

customers["customer_id"] = customers["customer_id"].astype(str).str.strip()
orders["customer_id"] = orders["customer_id"].astype(str).str.strip()

# -----------------------------
# KPI 1: Total Revenue
# -----------------------------
total_revenue = orders["total_amount"].sum()
print(f"\nTotal Revenue: ${total_revenue:,.2f}")

# -----------------------------
# KPI 2: Revenue by Category
# -----------------------------
category_rev = (
    orders.groupby("category")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)
print("\nRevenue by Category:\n", category_rev)

# -----------------------------
# KPI 3: Top 10 Selling Items
# -----------------------------
top_items = (
    orders.groupby("item_name")["quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 Selling Items:\n", top_items)

# -----------------------------
# KPI 4: Orders by Day of Week
# -----------------------------
orders_day = orders.groupby("day_of_week")["order_id"].count()
print("\nOrders by Day of Week:\n", orders_day)

# -----------------------------
# KPI 5: Orders by Channel
# -----------------------------
orders_channel = orders.groupby("order_channel")["order_id"].count()
print("\nOrders by Channel:\n", orders_channel)

# -----------------------------
# VISUALIZATION 1
# -----------------------------
plt.figure(figsize=(8, 5))
sns.barplot(x=category_rev.index, y=category_rev.values)
plt.title("Revenue by Category")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("analysis/revenue_by_category.png")
plt.close()

# -----------------------------
# VISUALIZATION 2
# -----------------------------
plt.figure(figsize=(10, 5))
sns.barplot(x=top_items.index, y=top_items.values)
plt.title("Top 10 Selling Items")
plt.ylabel("Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("analysis/top_10_items.png")
plt.close()

# -----------------------------
# VISUALIZATION 3
# -----------------------------
plt.figure(figsize=(8, 5))
sns.barplot(x=orders_day.index, y=orders_day.values)
plt.title("Orders by Day of Week")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("analysis/orders_by_day.png")
plt.close()

# =====================================================
# CUSTOMER SEGMENTATION (SAFE + ERROR-PROOF)
# =====================================================

# -----------------------------
# Create features ONLY from orders
# -----------------------------
customer_features = (
    orders.groupby("customer_id")
    .agg(
        visit_frequency=("order_id", "count"),
        avg_order_value=("total_amount", "mean"),
    )
    .reset_index()
)

# -----------------------------
# Merge features into customers
# -----------------------------
customers = customers.merge(
    customer_features, on="customer_id", how="left"
)

# -----------------------------
# GUARANTEED column creation
# -----------------------------
if "visit_frequency" not in customers.columns:
    customers["visit_frequency"] = 0
else:
    customers["visit_frequency"] = customers["visit_frequency"].fillna(0)

if "avg_order_value" not in customers.columns:
    customers["avg_order_value"] = 0
else:
    customers["avg_order_value"] = customers["avg_order_value"].fillna(0)

print("\nCustomer features sample:")
print(customers[["customer_id", "visit_frequency", "avg_order_value"]].head())

# -----------------------------
# END OF PHASE 3
# -----------------------------
print("\nPhase 3 completed successfully.")
print("KPIs calculated and charts saved in 'analysis/' folder.")

