# Write your MySQL query statement below
select query_name , 
round(avg(rating/position),2) AS quality ,
round(avg(if (rating<3,1,0)*100),2)AS poor_query_percentage
from Queries 
group by query_name