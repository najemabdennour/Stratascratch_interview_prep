# Import your libraries
import pandas as pd
# import the data
employee = pd.read_csv('employee.csv')
print(employee)
# Start writing code

res = employee[['first_name','bonus']][employee['bonus']<150]
print(res)
