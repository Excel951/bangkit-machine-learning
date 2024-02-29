import pandas as pd

product_df = pd.read_csv("product.csv")

product_df.isnull().sum()