# Import your libraries
import pandas as pd
# import the data
amazon_transactions = pd.read_csv('amazon_transactions.csv')
print(amazon_transactions)
# Start writing code
## solution 1 
#amazon_transactions.head()
#
##combine same dataframes using inner join
#amazon_combined = pd.merge(amazon_transactions, amazon_transactions, on="user_id", how="inner")
#
##above inner join gave duplicates- let's filter out the data
#amazon_combined['days'] = abs(amazon_combined['created_at_x'] - amazon_combined['created_at_y']).dt.days
#
##because of abs value the difference can be negative and hence duplicates needs to be removed in last step
#
##filtering data for days <=7 and ids not being same for 2 different items
#amazon_combined = amazon_combined[(amazon_combined.days <= 7) & (amazon_combined.id_x != amazon_combined.id_y)]
#
##final list of user_id as due to absolute difference there will be duplicates
#
#values = amazon_combined['user_id'].drop_duplicates()
#print(values)
## solution 2
import pandas as pd
import numpy as np
from datetime import datetime

amazon_transactions["created_at"] = pd.to_datetime(amazon_transactions["created_at"]).dt.strftime('%m-%d-%Y')
df = amazon_transactions.sort_values(by=['user_id', 'created_at'], ascending=[True, True])
df['prev_value'] = df.groupby('user_id')['created_at'].shift()
df['days'] = (pd.to_datetime(df['created_at']) - pd.to_datetime(df['prev_value'])).dt.days
result = df[df['days'] <= 7]['user_id'].unique()
print(result)