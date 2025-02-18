# Write your MySQL query statement below
select employee_id , case when (employee_id%2) <> 0
and  name not like 'M%' then salary
ELSE 0 END AS bonus
from Employees 
group by employee_id
order by employee_id