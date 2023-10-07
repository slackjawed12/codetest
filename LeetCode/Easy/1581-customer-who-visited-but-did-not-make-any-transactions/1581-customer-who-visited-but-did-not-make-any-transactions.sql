# Write your MySQL query statement below
SELECT
    v.customer_id as customer_id,
    count(*) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id is null
GROUP BY v.customer_id