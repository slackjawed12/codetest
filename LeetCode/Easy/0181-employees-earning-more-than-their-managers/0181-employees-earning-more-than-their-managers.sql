# Write your MySQL query statement below
select name as Employee 
from Employee e
join (
    select id, salary as managerSalary
    from Employee
    ) x
    on e.managerid = x.id
where salary > managerSalary