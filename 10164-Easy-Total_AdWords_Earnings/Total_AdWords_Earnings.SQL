select business_type,sum(adwords_earnings) 
from google_adwords_earnings
group by business_type;