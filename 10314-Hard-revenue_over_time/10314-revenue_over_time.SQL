select 
  year_month, 
  AVG(year_month_revenue) over(
    order by 
      year_month Rows between 2 preceding 
      and current row
  ) as rolling_avg 
from 
  (
    SELECT 
      to_char(created_at :: date, 'YYYY-MM') AS year_month, 
      sum(purchase_amt) AS year_month_revenue 
    FROM 
      amazon_purchases 
    WHERE 
      purchase_amt > 0 
    GROUP BY 
      year_month 
    ORDER BY 
      year_month
  ) ym_tbl 
order by 
  year_month asc
