# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
delete p from Person p
inner join (select min(id) as min_id, email from Person group by email) d
on p.email = d.email
where p.id!=d.min_id