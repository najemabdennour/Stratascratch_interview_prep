# Import your libraries
import pandas as pd
# import the data
employee = pd.read_csv("employee.csv")
print(employee)
# Start writing code
## Method 1
# Find duplicates on 'email' column
df = employee[employee.email.duplicated(keep=False)]
#df.email.iloc[0]
print(df)
# Find the df with duplicate rows removed.
df.email.drop_duplicates()
data = {'email': df[:1]['email'],'count':df['email'].count()}
res = pd.DataFrame(data)
print(res)