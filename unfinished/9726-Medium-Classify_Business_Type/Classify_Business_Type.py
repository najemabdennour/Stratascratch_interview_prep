# Import your libraries
import pandas as pd
# import the data
sf_restaurant_health_violations = pd.read_csv('sf_restaurant_health_violations.csv')
print(sf_restaurant_health_violations)
# Start writing code
df = sf_restaurant_health_violations
df['category']= df['business_name'].apply(lambda x : 'school' if x.lower().find('school') >= 0 
else 'restaurant' if x.lower().find('restaurant') >= 0
else 'cafe' if (x.lower().find('cafe') >= 0 or x.lower().find('coffee') >= 0 or x.lower().find('café') >= 0)
else 'other')
df = df[['business_name', 'category']]
print(df)
#df['café'] = df['business_name'].apply(lambda x: 'True' if x.lower().find('café') >= 0 else "")

#df[['business_name', 'category', 'café']]
#df.query('business_name == "café"')