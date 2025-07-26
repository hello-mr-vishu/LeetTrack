-- select *
-- from Employee e1
-- left join Employee e2
-- on e1.id = e2.id
-- group by e2.managerId

select name
from employee
where id in
(
Select managerId
from employee 
group by managerId
having count(managerId)>=5)
