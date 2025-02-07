# Write your MySQL query statement below
SELECT c.name as Customers
From Customers c
left join Orders o
on c.id =  o.customerId
where o.id is null 