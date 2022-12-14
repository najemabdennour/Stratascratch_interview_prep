# Import your libraries
import pandas as pd 

# import the data
fb_eu_energy = pd.read_csv('fb_eu_energy.csv')
fb_asia_energy = pd.read_csv('fb_asia_energy.csv')
fb_na_energy = pd.read_csv('fb_na_energy.csv')
print(fb_eu_energy)
print(fb_asia_energy)
print(fb_na_energy)
# Start writing code

concat = pd.concat([fb_eu_energy, fb_na_energy, fb_asia_energy])	
	
concat['date'] = pd.to_datetime(concat['date']).dt.strftime('%Y-%m-%d')

running_total = concat.groupby('date')['consumption'].sum().to_frame('running_total').reset_index()

running_total['total_consumption'] = running_total['running_total'].cumsum()

running_total['pct_total_consumption'] = round((running_total['total_consumption'] / running_total['running_total'].sum()) * 100)

running_total.drop('running_total', axis=1, inplace=True)

running_total

print(running_total)