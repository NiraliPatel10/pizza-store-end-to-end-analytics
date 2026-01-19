import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# -----------------------------
# CONFIGURATION
# -----------------------------
NUM_ORDERS = 50000
NUM_CUSTOMERS = 8000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2025, 12, 31)

random.seed(42)
np.random.seed(42)

# -----------------------------
# MENU MASTER
# -----------------------------
MENU = [
    ("Meat Feast Pizza", "Pizza", 20.79),
    ("Italiano Pizza", "Pizza", 20.79),
    ("Cheesy Pepperoni Pizza", "Pizza", 20.79),
    ("Chicken Parmesan Pizza", "Pizza", 20.79),
    ("BBQ Chicken Pizza", "Pizza", 20.79),
    ("Spicy Chicken Pizza", "Pizza", 20.79),
    ("Margherita Pizza", "Pizza", 19.99),
    ("Vegetarian Classic Pizza", "Pizza", 19.99),
    ("Farmhouse Classic Pizza", "Pizza", 20.79),
    ("Prawns Paradise Pizza", "Pizza", 20.79),
    ("Cheesy Garlic Bread", "Side", 11.99),
    ("Garlic Bread", "Side", 8.99),
    ("Caesar Salad", "Salad", 9.99),
    ("Wings (8 pcs)", "Wings", 22.98),
    ("Pasta Carbonara", "Pasta", 19.99),
    ("Soft Drink 1.25L", "Drink", 7.99)
]

SIZES = ["Small", "Medium", "Large"]
SIZE_MULTIPLIER = {"Small": 0.9, "Medium": 1.0, "Large": 1.2}
ORDER_CHANNELS = ["Walk-in", "Phone", "Online"]

# -----------------------------
# DATE GENERATOR
# -----------------------------
def random_date():
    delta = END_DATE - START_DATE
    return START_DATE + timedelta(days=random.randint(0, delta.days))

def random_time():
    hour = random.choices(
        population=[12,13,14,18,19,20,21,22],
        weights=[1,1,1,3,4,4,3,2]
    )[0]
    minute = random.randint(0, 59)
    return f"{hour:02d}:{minute:02d}"

# -----------------------------
# GENERATE ORDERS
# -----------------------------
orders = []

for order_id in range(1, NUM_ORDERS + 1):
    order_date = random_date()
    day_of_week = order_date.strftime("%A")
    item, category, base_price = random.choice(MENU)
    size = random.choice(SIZES) if category == "Pizza" else "Standard"
    quantity = random.randint(1, 4)
    channel = random.choice(ORDER_CHANNELS)

    price = base_price * SIZE_MULTIPLIER.get(size, 1)
    total_amount = round(price * quantity, 2)

    orders.append([
        order_id,
        random.randint(1, NUM_CUSTOMERS),
        order_date.date(),
        random_time(),
        day_of_week,
        item,
        category,
        size,
        quantity,
        channel,
        total_amount
    ])

orders_df = pd.DataFrame(orders, columns=[
    "Order_ID", "Customer_ID", "Order_Date", "Order_Time",
    "Day_of_Week", "Item_Name", "Category", "Size",
    "Quantity", "Order_Channel", "Total_Amount"
])

# -----------------------------
# GENERATE CUSTOMERS
# -----------------------------
customer_summary = orders_df.groupby("Customer_ID").agg(
    Visit_Frequency=("Order_ID", "count"),
    Avg_Order_Value=("Total_Amount", "mean"),
    Last_Visit_Date=("Order_Date", "max")
).reset_index()

preferred_items = (
    orders_df.groupby(["Customer_ID", "Item_Name"])
    .size()
    .reset_index(name="Count")
    .sort_values(["Customer_ID", "Count"], ascending=False)
    .drop_duplicates("Customer_ID")
)

preferred_channels = (
    orders_df.groupby(["Customer_ID", "Order_Channel"])
    .size()
    .reset_index(name="Count")
    .sort_values(["Customer_ID", "Count"], ascending=False)
    .drop_duplicates("Customer_ID")
)

customers_df = customer_summary.merge(
    preferred_items[["Customer_ID", "Item_Name"]],
    on="Customer_ID"
).merge(
    preferred_channels[["Customer_ID", "Order_Channel"]],
    on="Customer_ID"
)

customers_df.rename(columns={
    "Item_Name": "Preferred_Item",
    "Order_Channel": "Preferred_Channel"
}, inplace=True)

# -----------------------------
# EXPORT FILES
# -----------------------------
import os
os.makedirs("data/raw", exist_ok=True)
orders_df.to_csv("data/raw/orders.csv", index=False)
customers_df.to_csv("data/raw/customers.csv", index=False)

print("Dataset generation complete.")
print(f"Orders: {len(orders_df)}")
print(f"Customers: {len(customers_df)}")
