# Import your libraries
import pandas as pd
# import the data
facebook_web_log = pd.read_csv('facebook_web_log.csv')
facebook_web_log["timestamp"] = pd.to_datetime(facebook_web_log["timestamp"])#.dt.strftime('%m-%d-%Y')
print(facebook_web_log)
# Start writing code
df1 = facebook_web_log[facebook_web_log['action']=='page_load'].copy()
df1['day'] = df1['timestamp'].dt.date
df2 = facebook_web_log[facebook_web_log['action']=='page_exit'].copy()
df2['day'] = df2['timestamp'].dt.date

df = pd.merge(df1,df2,on='user_id')
df = df[df['day_x'] == df['day_y']]
df['diff'] = df['timestamp_y'] - df['timestamp_x']
df['diff'] = df['diff'].astype(int) /10**9 

result = df.groupby(['day_x','user_id']).min('diff')
#result =result.reset_index(drop=True)
result = result.groupby(['user_id']).mean('diff') 
print(result)
#print(result['user_id','diff'])
