CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    visit_frequency INTEGER,
    avg_order_value DECIMAL(10,2),
    preferred_item VARCHAR(100),
    preferred_channel VARCHAR(20),
    last_visit_date DATE
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    order_time TIME,
    day_of_week VARCHAR(10),
    item_name VARCHAR(100),
    category VARCHAR(20),
    size VARCHAR(20),
    quantity INTEGER,
    order_channel VARCHAR(20),
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
