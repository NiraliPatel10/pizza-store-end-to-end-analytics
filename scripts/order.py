import sqlite3
import pandas as pd

conn = sqlite3.connect("pizza_store.db")

customers = pd.read_sql("SELECT * FROM customers LIMIT 5", conn)
orders = pd.read_sql("SELECT * FROM orders LIMIT 5", conn)

print("Customers columns:", customers.columns.tolist())
print("Customers sample:\n", customers.head())

print("\nOrders columns:", orders.columns.tolist())
print("Orders sample:\n", orders.head())

conn.close()
