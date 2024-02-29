import pandas as pd
from sample_data import customers as customers_df, products as products_df, sales as sales_df, orders as orders_df

# Gathering data
# print(customers_df.head())
# print(products_df.head())
# print(sales_df.head())
# print(orders_df.head())

# Assessing data
# Customers
# print(customers_df.info())
# print(customers_df.isna().sum()) # missing value : 18
# print("Jumlah duplikasi data : {}".format(customers_df.duplicated().sum())) # duplicate data : 6
# print(customers_df.describe()) # there is inaccurate data

# Products
# print(products_df.info())
# print(products_df.isna().sum())
# print("Jumlah duplikasi data : {}".format(products_df.duplicated().sum())) # there is 6 duplicate data
# print(products_df.describe())

# Orders
# print(orders_df.info()) # there is fault type data on order_data and delivery_date
# print(orders_df.isna().sum())
# print("Jumlah duplikasi data : {}".format(orders_df.duplicated().sum()))
# print(orders_df.describe())

# Sales
# print(sales_df.info())
# print(sales_df.isna().sum()) # there is 19 missing values on total_price columns
# print("Jumlah duplikasi data : {}".format(sales_df.duplicated().sum()))
# print(sales_df.describe())


# Cleaning Data
# Customers
# Fixing duplicate data
customers_df.drop_duplicates(inplace=True) # drop duplicates data
# print("Jumlah duplikasi data : {}".format(customers_df.duplicated().sum())) # showed if duplicates data was removed
# Fixing missing values
# print(customers_df[customers_df.gender.isna()]) 
# print(customers_df.gender.value_counts()) # show the data that appears the most
customers_df.fillna(value="Prefer not to say", inplace=True) # fill missing values
# print(customers_df.isna().sum()) # show if missing values were removed
# Fixing inaccurate values
# print(customers_df[customers_df.age == customers_df.age.max()]) # check inaccurate data values
customers_df.age.replace(customers_df.age.max(), 70, inplace=True) # replace inaccurate values
# inaccurate values above can be assumed if there is human error
# print(customers_df[customers_df.age == customers_df.age.max()]) # check again inaccurate data values
customers_df.age.replace(customers_df.age.max(), customers_df.age.max()/10, inplace=True) # replace inaccurate values
# print(customers_df.describe()) # check again inaccurate data values

# Orders
datetime_columns = ['order_date', 'delivery_date'] # initialize columns that will be changed later

for column in datetime_columns:
    orders_df[column] = pd.to_datetime(orders_df[column]) # change type data columns into datetime
# print(orders_df.info()) # check type data columns

# Products
products_df.drop_duplicates(inplace=True) # drop duplicate data
# print(products_df.duplicated().sum()) # check duplicate data

# Sales
print(sales_df[sales_df.total_price.isna()]) # check where missing values
sales_df['total_price'] = sales_df['price_per_unit'] * sales_df['quantity'] # fill missing values)
print(sales_df.isna().sum()) # check where missing values
