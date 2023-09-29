# Write your MySQL query statement below
SELECT
      u.name,
      SUM(amount) AS balance
FROM Transactions t
JOIN Users u
ON t.account=u.account
GROUP BY t.account
HAVING SUM(amount) > 10000