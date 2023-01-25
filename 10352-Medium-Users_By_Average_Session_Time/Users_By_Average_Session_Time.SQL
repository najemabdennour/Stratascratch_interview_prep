select user_id, AVG(TIMESTAMPDIFF(SECOND, last_page_load , page_exit)) as session_time from (SELECT user_id, 
DATE(timestamp) As d,
MAX(CASE WHEN action ='page_load' THEN timestamp ELSE NULL END ) as last_page_load,
MIN(CASE WHEN action ='page_exit' THEN timestamp ELSE NULL END ) as page_exit
FROM facebook_web_log group by user_id, d) as a
group by user_id
HAVING session_time is not null; 