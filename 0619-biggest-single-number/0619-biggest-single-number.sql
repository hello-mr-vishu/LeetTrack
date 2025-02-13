# Write your MySQL query statement below

with cte AS 
(select num
FROM MyNumbers
group by num
Having count(num) =1)

select CASE WHEN count(*)>0 THEN  max(num)
ELSE NULL END as num
from cte