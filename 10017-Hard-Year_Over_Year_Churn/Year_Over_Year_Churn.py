# Import your libraries
import pandas as pd 
# import the data
lyft_drivers = pd.read_csv('lyft_drivers.csv')
print(lyft_drivers)
# Start writing code

lyft_drivers['end_date'] = pd.to_datetime(lyft_drivers['end_date']).dt.year

df = lyft_drivers.groupby('end_date')['index'].count().to_frame('current_churn').reset_index()

df['previous_churn'] = df['current_churn'].shift(1)

df =df.fillna(0)

df['churn_trends'] = (df['current_churn'] - df['previous_churn']).apply(lambda x: 'increase' if x > 0 else 'decrease' if x <0 else 'no change')

print(df)