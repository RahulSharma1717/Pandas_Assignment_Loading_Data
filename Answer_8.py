# What is the data type of the ratings column?

import pandas as pd

df = pd.read_csv('retail_data.csv')
print(type(df['Ratings']))


"""Output:
<class 'pandas.core.series.Series'>
"""