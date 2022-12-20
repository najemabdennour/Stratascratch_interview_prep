select owner_name, pe_description
from
los_angeles_restaurant_health_inspections 
where  pe_description like '%LOW RISK' 
and owner_name like '%BAKERY%'