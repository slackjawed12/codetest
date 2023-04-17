# Write your MySQL query statement below
select name as Customers
    from Customers c
    left outer join Orders o
    on c.id=o.customerId
where o.customerId is null