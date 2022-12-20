# Import your libraries
import pandas as pd
# import the data
los_angeles_restaurant_health_inspections = pd.read_csv("los_angeles_restaurant_health_inspections.csv")
print(los_angeles_restaurant_health_inspections)
# Start writing code
df = los_angeles_restaurant_health_inspections

df1 = df[(df['owner_name'].str.lower().str.find('baker') >= 0 ) & (df['pe_description'].str.lower().str.find('low risk') >= 0 )]
print(df1[['owner_name','pe_description']])