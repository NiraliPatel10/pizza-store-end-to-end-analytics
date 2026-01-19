import pandas as pd
import sqlite3
import os

# -----------------------------
# File Paths
# -----------------------------
db_path = "pizza_store.db"
customers_csv = "data/raw/customers.csv"
orders_csv = "data/raw/orders.csv"

# -----------------------------
# Connect to SQLite
# -----------------------------
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# -----------------------------
# Create Tables
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    visit_frequency INTEGER,
    avg_order_value REAL,
    preferred_item TEXT,
    preferred_channel TEXT,
    last_visit_date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    order_time TEXT,
    day_of_week TEXT,
    item_name TEXT,
    category TEXT,
    size TEXT,
    quantity INTEGER,
    order_channel TEXT,
    total_amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# -----------------------------
# Load CSVs
# -----------------------------
customers = pd.read_csv(customers_csv)
orders = pd.read_csv(orders_csv)

# -----------------------------
# Insert into SQLite
# -----------------------------
customers.to_sql("customers", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)

# -----------------------------
# Verify
# -----------------------------
print("Customers:", pd.read_sql("SELECT COUNT(*) FROM customers", conn).iloc[0,0])
print("Orders   :", pd.read_sql("SELECT COUNT(*) FROM orders", conn).iloc[0,0])

# -----------------------------
# Close Connection
# -----------------------------
conn.close()
print("Data import completed successfully!")
