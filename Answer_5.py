# What is the data type of df here?

import pandas as pd

df = pd.read_csv('retail_data.csv')
print(type(df))


"""Output:
<class 'pandas.core.frame.DataFrame'>
"""