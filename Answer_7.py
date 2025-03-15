# Display the ratings column from the dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
print(df['Ratings'])


"""Output:
0         5
1         4
2         2
3         4
4         1
         ..
293906    1
293907    5
293908    2
293909    4
293910    2
Name: Ratings, Length: 293911, dtype: int64
"""
