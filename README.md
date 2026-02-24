# Pizza Store End-to-End Analytics

## Business Objective
Analyze pizza store operations to optimize delivery, identify top-selling items, and understand customer behavior.

## Tools & Skills
- SQL: Aggregations, joins, window functions
- Python: Cleaning, EDA, segmentation
- Power BI: Dashboards, KPI visualization

## Dataset
- Orders table: order_id, customer_id, product_id, order_time, revenue
- Customers table: customer_id, location, loyalty_status
- Products table: product_id, name, category, price

## Approach
1. Data cleaning in Python
2. SQL queries for KPIs:
   - Total orders per product
   - Peak ordering hours
   - Revenue per location
3. Customer segmentation by order frequency & revenue
4. Power BI dashboard for visualization and interactivity

## Results & Insights
- Most orders placed between 6–9 PM
- Top 3 pizzas generate 60% of revenue
- High-value customers can be targeted for promotions

## Business Impact
- Optimized staff scheduling
- Targeted marketing campaigns
- Increased operational efficiency

## How to Run
- Import dataset into PostgreSQL
- Run SQL scripts from `/sql`
- Load PBIX dashboard for interactive visualization

## File Structure
- /data → CSV datasets
- /sql → SQL queries
- /notebooks → Python scripts
- /PowerBI → Dashboard files
