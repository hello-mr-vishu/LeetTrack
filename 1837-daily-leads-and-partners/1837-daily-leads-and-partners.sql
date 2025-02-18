# Write your MySQL query statement below
SELECT date_id , make_name, count(distinct lead_id) AS unique_leads ,count(distinct partner_id) AS unique_partners
from DailySales
Group by date_id , make_name
