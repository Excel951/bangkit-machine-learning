# cleaning method like "dropping" is good move if your data is very big (thousands data)
# but if your data is time series, you must rethinking to use this method

import pandas as pd

products_df = pd.read_csv('products.csv')

products_df.dropna(axis=0, inplace=True)