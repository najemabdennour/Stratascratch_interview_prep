select 
  worker_title 
from 
  (
    select 
      w.worker_id as worker_id, 
      w.salary as salary, 
      t.worker_ref_id as worker_ref_id, 
      t.worker_title as worker_title 
    from 
      worker w 
      left join title t on worker_id = worker_ref_id
  ) r 
where 
  salary = (
    select 
      max(salary) 
    from 
      worker
  )
