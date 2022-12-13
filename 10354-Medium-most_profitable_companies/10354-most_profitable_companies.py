# Import your libraries
import pandas as pd
# import the data
forbes_global_2010_2014 = pd.read_csv('forbes_global_2010_2014.csv')
print(forbes_global_2010_2014)
# start writing code
res = forbes_global_2010_2014.groupby('company')['profits'].sum().reset_index().sort_values(by='profits', ascending=False)
res = res[res['profits'].rank(method='max',ascending=False)<=3]
print(res)
