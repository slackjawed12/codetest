# Write your MySQL query statement below
SELECT 
    p.product_name as product_name,
    SUM(unit) as unit
FROM Products p
LEFT JOIN Orders o
ON p.product_id = o.product_id
WHERE o.order_date >= '2020-02-01' and o.order_date <= '2020-02-29'
GROUP BY p.product_id
HAVING SUM(unit)>=100