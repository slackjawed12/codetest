# Write your MySQL query statement below
select query_name, 
    ROUND(sum(rating/position)/count(*),2) as quality, 
    ROUND(sum(if(rating<3, 1, 0))/count(*)*100,2) as poor_query_percentage
from Queries
group by query_name
