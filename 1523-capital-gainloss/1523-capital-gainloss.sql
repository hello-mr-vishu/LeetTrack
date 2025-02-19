select stock_name , SUM(case when operation = 'BUY' 
then price*-1 else price end) AS capital_gain_loss
from stocks 
group by stock_name