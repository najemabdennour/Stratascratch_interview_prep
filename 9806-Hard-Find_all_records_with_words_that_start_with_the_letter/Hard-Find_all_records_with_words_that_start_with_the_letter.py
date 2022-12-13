# Import your libraries
import pandas as pd
import re
# import the data
google_word_lists = pd.read_csv('google_word_lists.csv')
print(google_word_lists)
# Start writing code
## solution 1
google_word_lists.head()

result = google_word_lists.loc[
    lambda x: (x.words1.str.contains("^g|,g")) | (x.words2.str.contains("^g|,g"))
]
print(result)

## solution 2 

# Start writing code
google_word_lists.head()
mark = [
    num
    for num, i in enumerate(google_word_lists["words1"])
    if bool(re.search("^g|,g", i))
]
mark1 = [
    num
    for num, i in enumerate(google_word_lists["words2"])
    if bool(re.search("^g|,g", i))
]
google_word_lists.iloc[mark + mark1, :]
print(google_word_lists)