# Write your MySQL query statement below
with cte as (
select * , DENSE_RANK() Over(order by salary desc) 
as r
From Employee)

select ifnull((select salary
from cte where r = 2 limit 1),null) as SecondHighestSalary