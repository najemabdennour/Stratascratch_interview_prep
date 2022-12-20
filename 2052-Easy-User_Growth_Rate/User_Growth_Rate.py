# Import your libraries
import pandas as pd
# import the data 
sf_events = pd.read_csv("sf_events.csv")
print(sf_events)
print(sf_events.dtypes)
sf_events['date'] = pd.to_datetime(sf_events.date)
print(sf_events.dtypes)
# Start writing code
df = sf_events
df['month'] = df['date'].dt.month

df1 = df.groupby(by = ['account_id', 'month'])['user_id'].apply(lambda x: len(x.unique())).reset_index()
#df.groupby(by = ['account_id', 'month'])['user_id'].agg('unique')

df2 = df1.pivot_table(index = 'account_id', columns = 'month', values = 'user_id').reset_index()

df2['rate'] = df2[1]/df2[12]
print(df2)
# method 2
df_1 = sf_events
df_1['m_y'] = df_1['date'].dt.strftime('%Y_%m')

df_2 = df_1.pivot_table(index = 'account_id', columns = 'm_y', values = 'user_id', aggfunc = 'nunique').reset_index().assign(rate = lambda df: df['2021_01'] / df['2020_12'] )

df_2[['account_id', 'rate']]
print(df_2)