# Import your libraries
import pandas as pd 
# import the data
airbnb_search_details = pd.read_csv("airbnb_search_details.csv")
print(airbnb_search_details)
# Start writing code
df = airbnb_search_details

df['total_amenities'] = df['amenities'].apply(lambda x: len(x.strip(',')))

result = df.groupby('city')['total_amenities'].sum().reset_index()

result = result.sort_values('total_amenities', ascending=False).reset_index()

result = result['city'][0]

print(result)