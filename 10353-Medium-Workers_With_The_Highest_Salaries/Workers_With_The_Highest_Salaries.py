# Import your libraries
import pandas as pd
# import the data 
worker = pd.read_csv('worker.csv')
title = pd.read_csv('title.csv')
# Start writing code
print(worker)
print(title)

df1 = pd.merge(worker, title, how = 'left', left_on = 'worker_id', right_on = 'worker_ref_id').sort_values('salary', ascending = False)

df2 = df1.query('salary == salary.max()')['worker_title']
res = df1[df1.salary == df1.salary.max()]['worker_title']
print(res)
print(df2)