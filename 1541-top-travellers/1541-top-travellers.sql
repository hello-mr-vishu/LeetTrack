# Write your MySQL query statement below
-- select name , distance as travelled_distance
-- from Users u
-- join Rides r
-- on u.id = r.user_id
-- order by distance DESC 

select distinct u.name , case when r.distance is not null
then sum(distance) over (partition by r.user_id order by r.user_id)
else 0 end as travelled_distance 
from Users u
left join Rides r
on u.id = r.user_id
order by travelled_distance desc , u.name