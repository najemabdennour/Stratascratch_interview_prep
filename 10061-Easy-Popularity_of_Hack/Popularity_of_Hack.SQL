select e.location,
avg(popularity) as average_popularity
from facebook_employees e
join facebook_hack_survey s
on e.id = s.employee_id
group by e.location;