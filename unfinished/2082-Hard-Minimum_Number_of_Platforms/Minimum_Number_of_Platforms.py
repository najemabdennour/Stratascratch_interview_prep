# Import your libraries
import pandas as pd
# import the data
train_arrivals = pd.read_csv("train_arrivals.csv")
train_departures = pd.read_csv("train_departures.csv")
print(train_arrivals)
print(train_departures)
# Start writing code
df1 = train_arrivals
df2 = train_departures

# Rename arrival_time and departure_time columns to time
df1 = df1.assign(marker = lambda df: 1).rename(columns = {'arrival_time' : 'time'})
df2 = df2.assign(marker = lambda df: -1).rename(columns = {'departure_time' : 'time'})

# Append df1 to df2
df3 = pd.concat([df1, df2]).sort_values(by = ['time']).assign(n_trains = lambda df: df.marker.cumsum())
# Select max value from n_trains
result = max(df3.n_trains)
print(result)