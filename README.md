# Aussinoz Pizza Store – End-to-End Analytics

## Project Overview
This project simulates a real-life analytics workflow for a suburban pizza store (Aussinoz Pizza, Salisbury, Brisbane). Using **two years of transactional data**, it demonstrates **business analysis and data analysis** skills applied to a real operational environment.

The analysis covers:
- Revenue and product performance
- Customer ordering patterns
- Sales channels
- Inventory and staffing insights
- Customer segmentation (optional)

---

## Tools & Technologies
- **SQL / SQLite**: Database management & KPI extraction  
- **Python**: Data cleaning, analysis, and visualization  
  - Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **VS Code**: IDE  
- **GitHub**: Version control & project portfolio

---

## Project Phases
### Phase 1: Dataset Creation
- Generated synthetic yet realistic datasets (`customers.csv` and `orders.csv`)  
- Captured 2 years of order history, including items, quantities, revenue, channels, and order dates

### Phase 2: SQL & KPIs
- Created SQLite database (`pizza_store.db`)  
- Designed `customers` and `orders` tables  
- Computed executive KPIs:
  - Total revenue
  - Revenue by category
  - Top-selling items
  - Orders by day of week
  - Orders by channel

### Phase 3: Python Analysis & Visualization
- Loaded SQL data into Pandas
- Built Python scripts for:
  - KPIs
  - Charts & dashboards
  - Optional customer segmentation
- Output charts saved in `/analysis/` folder

### Phase 4: Business Insights & Recommendations
- Interpreted data into actionable insights:
  - Product focus: top-selling pizzas
  - Channel optimisation: balance online, phone, walk-in
  - Staffing & inventory planning
- Provided executive-level recommendations

---

## Outputs
- SQL scripts: `create_tables.sql`, `kpi_queries.sql`
- Python scripts: `analysis.py`, `generate_data.py`
- Analysis charts: `/analysis/revenue_by_category.png`, `/analysis/top_10_items.png`, `/analysis/orders_by_day.png`, `/analysis/customer_segmentation.png`
- Executive insights & recommendations

---

## Learnings & Skills Demonstrated
- End-to-end analytics workflow (data → insight → recommendation)  
- KPI generation & visualization  
- Business-first thinking  
- Data-driven decision-making
- Customer segmentation & clustering

---

## Future Work
- Extend project to **sales forecasting** (Project 5)  
- Integrate with real POS system for live analytics  
- Deploy dashboards using Python or Power BI
