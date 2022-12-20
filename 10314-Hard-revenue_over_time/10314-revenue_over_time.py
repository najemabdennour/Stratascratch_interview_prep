# Import your libraries
import pandas as pd
import numpy as np
# import the data
amazon_purchases = pd.read_csv('amazon_purchases.csv')
print(amazon_purchases)
print(amazon_purchases.dtypes)
amazon_purchases['created_at']= pd.to_datetime(amazon_purchases.created_at)
print(amazon_purchases.dtypes)

# start writing code
# method 1
amazon_purchases = amazon_purchases[amazon_purchases['purchase_amt']>=0].reset_index(drop=True)
amazon_purchases['year_month'] = pd.to_datetime(amazon_purchases['created_at']).dt.to_period('M')
mnth_grpby = amazon_purchases.groupby('year_month',as_index=False)['purchase_amt'].sum()
mnth_grpby = mnth_grpby.set_index('year_month')
mnth_grpby = mnth_grpby.sort_index()
result = mnth_grpby.rolling(window=3,min_periods=1).mean().reset_index()
print(result)

# Method 2
df = amazon_purchases
df['year_month'] = df['created_at'].dt.strftime('%Y-%m')
df1 = df[df['purchase_amt'] > 0]

df2 = df1.pivot_table(columns = 'year_month', values = 'purchase_amt', aggfunc = 'sum').melt()

df2['3-month'] = df2['value'].rolling(3).mean()
print(df2)
#rolling window calculation example
df_ex = pd.DataFrame({'B' : [0.0, 1.0, 2.0, np.nan, 4.0]})

#Rolling sum with a window length of 2 observations.
df_ex['B'].rolling(2).mean()

#Rolling sum with a window length of 2 observations, but only needs a minimum of 1 observation to calculate a value.
df_ex['B'].rolling(2, min_periods = 1).mean()
