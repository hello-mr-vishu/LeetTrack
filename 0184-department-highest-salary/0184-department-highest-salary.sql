# Write your MySQL query statement below
with cte as 
(select d.name as Department, e.name as Employee ,e.salary as Salary ,MAX(e.salary) OVER (partition by e.departmentId ) as max_salary
from Employee e
left join Department d
on e.departmentId = d.id
)
select department , employee , salary 
from cte 
where salary = max_salary