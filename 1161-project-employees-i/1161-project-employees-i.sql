# Write your MySQL query statement below
SELECT project_id ,round(avg(e.experience_years),2) AS average_years
from Project p
left join Employee e
on p.employee_id = e.employee_id
group by p.project_id 