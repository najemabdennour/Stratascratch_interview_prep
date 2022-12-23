SELECT
    COUNT(DISTINCT user_id) total_users
FROM
(
    SELECT
        user_id, created_at, 
        DENSE_RANK() OVER(partition by user_id order by created_at) date_rnk,
        DENSE_RANK() OVER(partition by user_id, product_id order by created_at) product_rnk
    FROM marketing_campaign
) t1
WHERE date_rnk > 1 AND product_rnk = 1