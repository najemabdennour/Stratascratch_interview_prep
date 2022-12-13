select company,profits from (SELECT company,profits as profits,dense_rank() over ( order by profits desc nulls first) ranks  FROM forbes_global_2010_2014) as t where ranks <4
