# -----------------------------
# Project 5: Sales Forecasting
# -----------------------------
# Predict daily and weekly revenue for Aussinoz Pizza Store
# -----------------------------

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import os
import sqlite3

# -----------------------------
# Ensure analysis folder exists
# -----------------------------
os.makedirs("analysis", exist_ok=True)

# -----------------------------
# Load orders from SQLite DB
# -----------------------------
conn = sqlite3.connect("pizza_store.db")
orders = pd.read_sql("SELECT * FROM orders", conn)
conn.close()

# -----------------------------
# Normalize column names
# -----------------------------
orders.columns = orders.columns.str.lower().str.replace(' ', '_')

# -----------------------------
# Ensure proper data types
# -----------------------------
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders['total_amount'] = pd.to_numeric(orders['total_amount'], errors='coerce')
orders = orders.dropna(subset=['total_amount', 'order_date'])

# -----------------------------
# Aggregate daily revenue
# -----------------------------
daily_sales = orders.groupby("order_date").agg(
    daily_revenue=("total_amount", "sum")
).reset_index()

if daily_sales.empty:
    raise Exception("No daily sales data available for forecasting!")

# -----------------------------
# Feature: day index for regression
# -----------------------------
daily_sales['day_index'] = range(len(daily_sales))
X = daily_sales[['day_index']]
y = daily_sales['daily_revenue']

# -----------------------------
# Train/Test split (80/20)
# -----------------------------
train_size = int(len(X)*0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# -----------------------------
# Train Linear Regression Model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# -----------------------------
# Evaluate model
# -----------------------------
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Forecast RMSE: ${rmse:,.2f}")

# -----------------------------
# Visualization: Daily Revenue Forecast
# -----------------------------
plt.figure(figsize=(12,6))
plt.plot(daily_sales['order_date'], y, label='Actual Revenue', color='blue')
plt.plot(daily_sales['order_date'].iloc[train_size:], y_pred, label='Predicted Revenue', color='red', linestyle='--')
plt.title("Daily Revenue Forecast")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("analysis/revenue_forecast.png")
plt.close()

# -----------------------------
# Aggregate weekly revenue
# -----------------------------
daily_sales['week'] = daily_sales['order_date'].dt.isocalendar().week
weekly_sales = daily_sales.groupby('week').agg(
    weekly_revenue=('daily_revenue', 'sum')
).reset_index()

plt.figure(figsize=(12,6))
plt.plot(weekly_sales['week'], weekly_sales['weekly_revenue'], marker='o', color='green')
plt.title("Weekly Revenue Trend")
plt.xlabel("Week Number")
plt.ylabel("Revenue ($)")
plt.xticks(weekly_sales['week'])
plt.tight_layout()
plt.savefig("analysis/weekly_forecast.png")
plt.close()

# -----------------------------
# Insights
# -----------------------------
peak_week = weekly_sales.loc[weekly_sales['weekly_revenue'].idxmax()]
low_week = weekly_sales.loc[weekly_sales['weekly_revenue'].idxmin()]

print("\nInsights:")
print(f"- Peak revenue week: Week {peak_week['week']} with ${peak_week['weekly_revenue']:,.2f}")
print(f"- Lowest revenue week: Week {low_week['week']} with ${low_week['weekly_revenue']:,.2f}")
print("\nForecasting complete. Plots saved in 'analysis/' folder.")
