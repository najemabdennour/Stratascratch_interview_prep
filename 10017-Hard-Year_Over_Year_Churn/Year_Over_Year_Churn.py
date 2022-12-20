# Import your libraries
import pandas as pd 
import numpy as np
# import the data
lyft_drivers = pd.read_csv('lyft_drivers.csv')
print(lyft_drivers)
print(lyft_drivers.dtypes)
lyft_drivers['end_date'] = pd.to_datetime(lyft_drivers['end_date'])
lyft_drivers['start_date'] = pd.to_datetime(lyft_drivers['start_date'])
print(lyft_drivers.dtypes)

# Start writing code

lyft_drivers['end_date'] = pd.to_datetime(lyft_drivers['end_date']).dt.year
df = lyft_drivers.groupby('end_date')['index'].count().to_frame('current_churn').reset_index()

df['previous_churn'] = df['current_churn'].shift(1)

df =df.fillna(0)

df['churn_trends'] = (df['current_churn'] - df['previous_churn']).apply(lambda x: 'increase' if x > 0 else 'decrease' if x <0 else 'no change')

print(df)
# method 2
yoyc = lyft_drivers
#yoyc['end_year'] = yoyc['end_date'].dt.year
yoyc.query('end_date == "2018"').shape[0]
#df2 = df.dropna(subset = ['end_year'])

df1 = yoyc.pivot_table(columns = 'end_date', values = 'index', aggfunc = 'count').melt()

#print(df1)
#df1.melt(var_name = 'ey', value_name = 'count')
df1['pre'] = df1.value.shift(1).fillna(0)

#df1['cmpr'] = (df1['value'] > df1['pre']).apply(lambda x: 'increase' if x == True else 'decrease')

#df1['cmpr'] = df1.assign(cmpr = lambda x: x[['vaule', 'pre']].apply(lambda y: 'increase' if y.value > y.pre else 'crease' ))

df1['cmp'] = np.where(df1.value > df1.pre, 'increase', np.where(df1.value == df1.pre, 'no change', 'decrease'))

print(df1)