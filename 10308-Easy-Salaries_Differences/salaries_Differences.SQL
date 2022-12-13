with sal_dept as (select max(sal) as max_salary,dept
from (select db_employee.salary as sal,db_dept.department as dept from db_employee left join db_dept on db_employee.department_id = db_dept.id) as t1 
where dept in('engineering','marketing') group by dept)
select ABS(e.max_salary - m.max_salary) from sal_dept e,sal_dept m where e.dept = 'engineering' and m.dept = 'marketing'
