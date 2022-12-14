# Import your libraries
import pandas as pd
# import the data
facebook_employees = pd.read_csv('facebook_employees.csv')
facebook_hack_survey = pd.read_csv('facebook_hack_survey.csv')
print(facebook_employees)
print(facebook_hack_survey)
# Start writing code

merge = pd.merge(left = facebook_employees,right = facebook_hack_survey,left_on = 'id',right_on = 'employee_id')
merge.head()
merge.groupby(by='location').agg({'location':'max','popularity':'mean'})
print(merge)