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


# using the approach to concatenate adding all dataframe along rows
fb_final = pd.concat([fb_eu_energy,fb_asia_energy,fb_na_energy],axis=0)
fb_grouped = fb_final.groupby(['date']).agg(['sum'])


##converting the grouped data into dataframe
fb_grouped.columns = [ ' '.join(str(i) for i in col) for col in fb_grouped.columns]
fb_grouped.reset_index(inplace=True)


#obtaining max value of consumption
max_cons = max(fb_grouped['consumption sum'])

#subsetting based on max value of consumption
fb_max_df = fb_grouped[fb_grouped['consumption sum'] == max_cons]
print(fb_max_df)