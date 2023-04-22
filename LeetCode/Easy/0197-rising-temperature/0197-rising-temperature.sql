# Write your MySQL query statement below
select w.id
from Weather w
join Weather y
on w.recordDate=date_add(y.recordDate, interval 1 day)
where w.temperature>y.temperature