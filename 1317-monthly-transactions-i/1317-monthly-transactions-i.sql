# Write your MySQL query statement below
SELECT 
date_format(trans_date,'%Y-%m') as month    ,
 country ,
count(id) AS trans_count,
sum(if(state = 'approved',1,0)) AS approved_count ,
sum(amount) AS trans_total_amount ,
sum(if(state= 'approved',amount,0 ))  AS approved_total_amount 
from Transactions
group by month , country