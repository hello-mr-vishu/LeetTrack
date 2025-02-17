# Write your MySQL query statement below
SELECT sell_date , count(distinct product) AS num_sold ,
GROUP_CONCAT(DISTINCT product ORDER BY product) AS products
From Activities
group by sell_date