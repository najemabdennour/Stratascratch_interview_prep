select distinct user_id 
from (select *, 
    lead(created_at) over(partition by user_id order by created_at) as next_purchase
    from amazon_transactions) sbqry
where datediff(next_purchase, created_at) <= 7;