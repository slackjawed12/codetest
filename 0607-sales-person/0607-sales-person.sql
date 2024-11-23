# Write your MySQL query statement below
SELECT DISTINCT name
FROM SalesPerson
WHERE name NOT IN (SELECT DISTINCT s.name
FROM SalesPerson s
LEFT JOIN Orders o 
ON o.sales_id=s.sales_id
LEFT JOIN Company c
ON o.com_id=c.com_id
WHERE c.name='RED')

