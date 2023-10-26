# Write your MySQL query statement below
SELECT *
FROM Users
WHERE mail REGEXP('^[a-zA-Z]{1}[a-zA-Z0-9\\.\\-_]*@leetcode\\.com$')