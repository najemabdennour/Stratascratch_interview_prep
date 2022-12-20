SELECT
    email, COUNT(*)
FROM
    employee
GROUP BY
    email
HAVING 
    COUNT(*) > 1