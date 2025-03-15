# Display columns product category, product brand, product type, and products without using another variable.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df[['Product_Category', 'Product_Brand', 'Product_Type', 'products']])


"""Output:
       Product_Category  Product_Brand Product_Type            products
0              Clothing           Nike       Shorts      Cycling shorts
1           Electronics        Samsung       Tablet          Lenovo Tab
2                 Books  Penguin Books   Children's    Sports equipment
3            Home Decor     Home Depot        Tools       Utility knife
4               Grocery         Nestle    Chocolate   Chocolate cookies
...                 ...            ...          ...                 ...
293906            Books  Penguin Books      Fiction  Historical fiction
293907      Electronics          Apple       Laptop             LG Gram
293908         Clothing         Adidas       Jacket               Parka
293909       Home Decor           IKEA    Furniture            TV stand
293910       Home Decor     Home Depot  Decorations              Clocks

[293911 rows x 4 columns]
"""