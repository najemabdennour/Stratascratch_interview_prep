# Import your libraries
import pandas as pd
# import the data
doordash_delivery = pd.read_csv('doordash_orders.csv')
print(doordash_delivery)
print(doordash_delivery.dtypes)
doordash_delivery['order_timestamp'] = pd.to_datetime(doordash_delivery.order_timestamp)
print(doordash_delivery.dtypes)
# Start writing code
df = doordash_delivery

df['day_of_week'] = df['order_timestamp'].dt.weekday+1

df['hours'] = df['order_timestamp'].dt.hour

#df.groupby('day_of_week')['hours','order_total'].apply(lambda x: x.order_total.sum()/x.hours.sum()).reset_index(name = 'rate')

df = df.groupby(by = ['day_of_week', 'hours'], as_index = False).agg({'total_amount_earned': 'max'})
print(df)