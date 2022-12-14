# Import your libraries
import pandas as pd
# import the data
google_adwords_earnings = pd.read_csv('google_adwords_earnings.csv')
print(google_adwords_earnings)
# Start writing code

res = google_adwords_earnings.groupby('business_type',as_index = False).agg({"adwords_earnings":"sum"})
print(res)