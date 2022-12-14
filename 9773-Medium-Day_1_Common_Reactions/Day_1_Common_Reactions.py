# Import your libraries
import pandas as pd 
# import the data
facebook_reactions= pd.read_csv('facebook_reactions.csv')
print(facebook_reactions)
# Start writing code
df = facebook_reactions
df = df[df['date_day'] == 1]

df = df.groupby('reaction').size().to_frame('n_reactions').reset_index().sort_values('n_reactions', ascending=False)

result = df[df['n_reactions'] == df['n_reactions'].max()]
print(result)