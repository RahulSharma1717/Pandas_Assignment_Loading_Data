# What is the data type of data variable from the above code?

import pandas as pd

data = pd.read_csv('retail_data.csv')
print(type(data))


"""Output:
<class 'pandas.core.frame.DataFrame'>
"""