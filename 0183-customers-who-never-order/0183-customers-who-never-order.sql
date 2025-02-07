# Write your MySQL query statement below
SELECT name as Customers
from customers
where id not in (
    select customerId 
    from Orders
)