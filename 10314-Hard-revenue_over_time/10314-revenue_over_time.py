# Import your libraries
import pandas as pd
import numpy as np
# import the data
amazon_purchases = pd.read_csv('amazon_purchases.csv')
print(amazon_purchases)
# start writing code
amazon_purchases = amazon_purchases[amazon_purchases['purchase_amt']>=0].reset_index(drop=True)
amazon_purchases['year_month'] = pd.to_datetime(amazon_purchases['created_at']).dt.to_period('M')
mnth_grpby = amazon_purchases.groupby('year_month',as_index=False)['purchase_amt'].sum()
mnth_grpby = mnth_grpby.set_index('year_month')
mnth_grpby = mnth_grpby.sort_index()
result = mnth_grpby.rolling(window=3,min_periods=1).mean().reset_index()
print(result)