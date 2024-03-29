--Find the most common reaction for day 1 by counting the number of occurrences for each reaction. Output the reaction alongside its number of occurrences.

WITH cte AS (
SELECT reaction, 
       COUNT(*) AS n_reactions, 
       RANK() OVER (ORDER BY COUNT(*) DESC) AS reaction_rank
    FROM facebook_reactions 
WHERE date_day = 1 
GROUP BY reaction) 

SELECT reaction, 
       n_reactions
    FROM cte 
WHERE reaction_rank = 1 