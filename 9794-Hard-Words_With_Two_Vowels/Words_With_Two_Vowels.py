# Import your libraries
import pandas as pd 
import numpy as np
# import the data
google_word_lists = pd.read_csv('google_word_lists.csv')
print(google_word_lists)

def two_vowels(word): 
    vowels = [i for i in word if i in {'a', 'e', 'i', 'o', 'u'}]
    return len(vowels) == 2 

w1 = google_word_lists['words1'].apply(lambda x: x.split(',')).explode()

w2 = google_word_lists['words2'].apply(lambda x: x.split(',')).explode()

w1 = pd.DataFrame(w1).rename(columns={'words1':'word'})
w2 = pd.DataFrame(w2).rename(columns={'words2':'word'})
df = pd.concat([w1, w2],ignore_index=True).drop_duplicates()
result = df['word'].apply(lambda x: x if two_vowels(x) == 1 else np.nan)

result = result.dropna()

print(result)