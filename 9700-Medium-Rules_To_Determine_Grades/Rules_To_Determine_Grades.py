# Import your libraries
import pandas as pd 
# import the data
los_angeles_restaurant_health_inspections = pd.read_csv('los_angeles_restaurant_health_inspections.csv')
print(los_angeles_restaurant_health_inspections)
# Start writing code
df = los_angeles_restaurant_health_inspections

df = df.groupby('grade')['score'].agg(min_score='min', max_score = 'max').reset_index()

df['rule'] = "Score > " + (df['min_score'] - 1).astype(str) + " And Score < " + df['max_score'].astype(str) + " => Grade = " + df['grade'].astype(str)

print(df)