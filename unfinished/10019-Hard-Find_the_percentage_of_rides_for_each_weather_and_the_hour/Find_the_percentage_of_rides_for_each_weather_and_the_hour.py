# Import your libraries
import pandas as pd
# impor the data
lyft_rides = pd.read_csv('lyft_rides.csv')
print(lyft_rides)
# Start writing code
df1 = lyft_rides
## Method 1
# Find out the number of rides by the each combination of the weather and the hour
df1['c'] = df1.groupby(['weather', 'hour'])['index'].transform('count')

#Calculate probability
df1['p'] = df1['c']/len(df1)
#df2 = df1.query('weather == "cloudy" & hour == 7')

# Sort df
res1 = df1.sort_values(by = ['weather', 'hour'], ascending = True)[['weather', 'hour', 'c', 'p']].drop_duplicates()
print(res1)
## Method 2
# Find out the number of rides for each combination of the weather and hour
df3 = df1.groupby(['weather', 'hour'], as_index = False).agg({'index' : 'count'}).rename(columns = {'index' : 'count'})

# Find the probability by dividing these count by the total number of occurrences (n of rows in the df1)

df3['p'] = df3['count']/len(df1)

# Sort the df

df3.sort_values(['weather', 'hour'], ascending = True)
print(df3)