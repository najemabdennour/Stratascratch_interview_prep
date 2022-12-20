# Import your libraries
import pandas as pd
# import the data
submissions = pd.read_csv('submissions.csv')
print(submissions)
# Start writing code
submissions['total']=submissions.groupby('rate_type')['balance'].transform('sum')

submissions['p'] = submissions['balance']/submissions['total']

print(submissions)