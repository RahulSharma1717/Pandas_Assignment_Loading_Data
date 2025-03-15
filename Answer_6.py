# Display the 'products' column from the dataset.

import pandas as pd

df = pd.read_csv('retail_data.csv')
print(df['products'])


"""Output:
0             Cycling shorts
1                 Lenovo Tab
2           Sports equipment
3              Utility knife
4          Chocolate cookies
                 ...        
293906    Historical fiction
293907               LG Gram
293908                 Parka
293909              TV stand
293910                Clocks
Name: products, Length: 293911, dtype: object
"""