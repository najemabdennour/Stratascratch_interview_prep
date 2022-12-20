# Import your libraries
import pandas as pd
# import the data
los_angeles_restaurant_health_inspections = pd.read_csv('los_angeles_restaurant_health_inspections.csv')
print(los_angeles_restaurant_health_inspections)
# Start writing code
df = los_angeles_restaurant_health_inspections

df2=df[df['grade'] == 'A'][['score', 'grade']]

variance = ((df2['score'] - df2['score'].mean())**2).mean()

deviation = variance**0.5

df3 = pd.DataFrame({'variance': [variance], 'std_deviation' : [deviation]})
print(df3)
#method 2 using built-in Pandas Statistical Methods
var = df[df['grade']=='A']['score'].var(ddof = 0)

stdev = df[df['grade'] == 'A']['score'].std(ddof = 0)

df4 = pd.DataFrame({'var': [var], stdev : [stdev]})
print(df4)