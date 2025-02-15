# Write your MySQL query statement below
with cte as 
(SELECT query_name , rating/position AS ratio, CASE WHEN 
rating<3 THEN 1
ELSE 0 END AS quality_binary
From Queries)

SELECT query_name , ROUND(AVG(ratio),2) AS 
quality, round((SUM(quality_binary)/count(*))*100,2) AS
poor_query_percentage
FROM cte
group by query_name 