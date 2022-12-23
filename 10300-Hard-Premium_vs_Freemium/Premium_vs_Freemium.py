# Import your libraries
import pandas as pd
import numpy as np
# import the data 
ms_user_dimension = pd.read_csv('ms_user_dimension.csv')
ms_acc_dimension = pd.read_csv('ms_acc_dimension.csv')
ms_download_facts = pd.read_csv('ms_download_facts.csv')
print(ms_user_dimension)
print(ms_acc_dimension)
print(ms_download_facts)
# Start writing code
df1 = ms_user_dimension.drop_duplicates()
df2 = ms_acc_dimension.drop_duplicates()
df3 = ms_download_facts.drop_duplicates()

df4 = pd.merge(df1,df2, how = 'left', on = 'acc_id')
df5 = pd.merge(df4, df3, how = 'left', on = 'user_id').drop_duplicates()

df6 = df5.groupby(['paying_customer','date'])['downloads'].sum().reset_index(name = 'n_downloads')

df7 = df6.query('paying_customer == "no"')[['date', 'n_downloads']].rename(columns = {"n_downloads":"non-paying downloads"})

df8 = df6[df6.paying_customer == "yes"][['date', 'n_downloads']].rename(columns = {"n_downloads" : 'paying downloads'})

df9 = pd.merge(df7, df8, how = 'left', on = 'date').sort_values('date')

res = df9[df9['non-paying downloads'] > df9['paying downloads']]

#using piovt to spread columns to rows
df6.pivot(index = 'date', columns = 'paying_customer', values = 'n_downloads').reset_index()

#using piovt_table to add agg func
results = df5.pivot_table(index = 'date', columns = 'paying_customer', values = 'downloads', aggfunc = np.sum).reset_index().query('no > yes')
print(results)