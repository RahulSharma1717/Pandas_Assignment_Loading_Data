# Load the data by specifying a delimiter.

import pandas as pd

df = pd.read_csv('retail_data.csv', delimiter=',')
print(df)


"""Output:
        Transaction_ID  Customer_ID  ... Ratings            products
0              8691788        37249  ...       5      Cycling shorts
1              2174773        69749  ...       4          Lenovo Tab
2              6679610        30192  ...       2    Sports equipment
3              7232460        62101  ...       4       Utility knife
4              4983775        27901  ...       1   Chocolate cookies
...                ...          ...  ...     ...                 ...
293906         4246475        12104  ...       1  Historical fiction
293907         1197603        69772  ...       5             LG Gram
293908         7743242        28449  ...       2               Parka
293909         9301950        45477  ...       4            TV stand
293910         2882826        53626  ...       2              Clocks

[293911 rows x 30 columns]
"""