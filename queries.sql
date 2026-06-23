SELECT
    SUM("Sales") AS total_sales
FROM sales;
SELECT
    "State",
    ROUND(SUM("Sales")::numeric, 2) AS total_sales
FROM sales
GROUP BY "State"
ORDER BY total_sales DESC
LIMIT 10;

DROP VIEW IF EXISTS sales_by_state;
CREATE VIEW sales_by_state AS
SELECT
    "State",
    ROUND(SUM("Sales")::numeric, 2) AS total_sales,
    ROUND(SUM("Profit")::numeric, 2) AS total_profit
FROM sales
GROUP BY "State";

SELECT *
FROM sales_by_state
ORDER BY total_sales DESC;