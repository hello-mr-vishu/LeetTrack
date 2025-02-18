select product_id 
from Products
-- group by product_id
where low_fats = 'Y'
AND recyclable = 'Y'