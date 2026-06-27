## **Retail Sales Analytics Dashboard** 
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

### Business Problem

Retail organizations regularly track sales, but identifying meaningful business trends from thousands of individual transactions can be difficult. Leaders need a clear view of overall performance while also being able to identify which products, customer segments, and regions contribute the greatest value.

This project answers several business questions.

Which states generate the highest sales and profit?
Which product categories contribute the most to profitability?
Which customer segments generate the most revenue?
How have sales and profits changed over time?
Which customers contribute the greatest share of total sales?



The dataset was cleaned and transformed using Python, loaded into PostgreSQL for querying, and visualized in Power BI through an interactive dashboard.



The dashboard provides insights into:



* Total Sales
* Total Profit
* Order Volume
* Average Shipping Time
* Monthly Sales Trends
* Top Performing States
* Product Category Performance
* Customer Profitability
* Segment Analysis

### Data Preparation

Before any analysis was performed, the dataset was cleaned and transformed using Python to improve data quality and prepare it for reporting.

The preparation process included correcting data types, creating calculated fields, organizing the data into a consistent structure, and loading the cleaned dataset into PostgreSQL for analysis.

### **Dashboard Screenshots**

Retail Sales Overview

The first dashboard page provides a high level summary of business performance. It includes key performance indicators for sales, profit, total orders, and average shipping time while also displaying monthly sales trends, top performing states, sales by category, and sales by customer segment.

![Retail Sales Overview](page1_dashboard.png)

Users can apply interactive regional filters to compare performance across different parts of the business.

![Region Filter Example](interactive_regions_screenshot.png)



Profitability and Customer Analysis

The second dashboard focuses on profitability and customer behavior. It highlights monthly profit trends, compares profit across customer segments and product categories, identifies top customers by sales, and allows users to explore geographic performance through an interactive map.

![Profitability & Customer Analysis](page2_dashboard.png)

The dashboard can also be filtered to analyze individual regions or states.

![New York Region Example](interactive_regions_newyork_screenshot.png)


### Key Findings

The analysis identified several important business trends.

California is one of the company's strongest areas and a crucial area for future client retention strategies because it produced the highest overall revenue.

Product profitability does not always correspond with total sales volume and should be taken into account independently when assessing performance, as evidenced by the fact that technology items generated the highest overall profit.

The consumer category produced the highest revenue share, suggesting that it is the company's main clientele.

A very small number of clients provided a disproportionately big amount of overall sales, according to customer purchasing habits, underscoring the significance of preserving connections with high-value customers.

Trends in monthly sales and profits showed steady business growth over the examined time frame.
