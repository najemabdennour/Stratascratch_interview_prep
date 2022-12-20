# Import your libraries
import pandas as pd
# import the data
sf_public_salaries = pd.read_csv('sf_public_salaries.csv')
print(sf_public_salaries)
# Start writing code
df = sf_public_salaries
df1 = df[df.year == 2012].sort_values(['totalpaybenefits'])

# Append top 5 rows to least 5 rows 
df2 = pd.concat([df1[:5], df1[-5:]])

# Append first 5 columns to last 5 columns
df3 = pd.concat([df1.iloc[:, :5], df1.iloc[:, -5:]], axis =1)

#indexing, row names are the same as the row indices
#df.loc[0:2, 'id':'jobtitle']

#df.iloc[0:2, 0:2]
print(df3)