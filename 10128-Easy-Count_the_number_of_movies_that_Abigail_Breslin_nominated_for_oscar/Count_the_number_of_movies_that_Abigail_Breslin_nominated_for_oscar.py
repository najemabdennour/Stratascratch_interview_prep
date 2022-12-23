# Import your libraries
import pandas as pd
# import the data 
oscar_nominees = pd.read_csv('oscar_nominees.csv')
print(oscar_nominees)
#filter Tricks
df1 = oscar_nominees.query('id == "1" | year == "2000"')
oscar_nominees[oscar_nominees.id.isin(["1", "2"])]
oscar_nominees[(oscar_nominees['id'] == 1) | (oscar_nominees['id'] == 2)] 
oscar_nominees[oscar_nominees['id'].isin([2,3])]
df_res = oscar_nominees.query('nominee == "Abigail Breslin"').groupby('movie').size().reset_index()
res = oscar_nominees.groupby('nominee').size().reset_index().query('nominee == "Abigail Breslin"')
print(df_res)