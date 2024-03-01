import pandas as pd
from sample_data import customers as customers_df, products as products_df, sales as sales_df, orders as orders_df

# FROM latihan_data_wrangling
# =================================================================
customers_df.drop_duplicates(inplace=True) # drop duplicates data
customers_df.fillna(value="Prefer not to say", inplace=True) # fill missing values
customers_df.age.replace(customers_df.age.max(), 70, inplace=True) # replace inaccurate values
customers_df.age.replace(customers_df.age.max(), customers_df.age.max()/10, inplace=True) # replace inaccurate values
datetime_columns = ['order_date', 'delivery_date'] # initialize columns that will be changed later
for column in datetime_columns:
    orders_df[column] = pd.to_datetime(orders_df[column]) # change type data columns into datetime
products_df.drop_duplicates(inplace=True) # drop duplicate data
# print(sales_df[sales_df.total_price.isna()]) # check where missing values
sales_df['total_price'] = sales_df['price_per_unit'] * sales_df['quantity'] # fill missing values)
# print(sales_df.isna().sum()) # check where missing values
# =================================================================


# print(customers_df.describe(include='all'))
# print('\n================================================\n')
# print(customers_df.groupby(by='gender').agg({
#     'customer_id': 'nunique',
#     'age': ['max', 'min', 'mean', 'std'],
# }))
# print('\n================================================\n')
# print(customers_df.groupby(by='city').customer_id.nunique().sort_values(ascending=False))
# print('\n================================================\n')
# print(customers_df.groupby(by='state').customer_id.nunique().sort_values(ascending=False))
# print('\n================================================\n')

delivery_time = orders_df["delivery_date"] - orders_df["order_date"] # initialize delivery_time with delivery_date - order_date
delivery_time = delivery_time.apply(lambda x: x.total_seconds()) # operation to each element in column of DataFrame or Series
orders_df["delivery_time"] = round(delivery_time/86400) # set delivery_time (day) in DataFrame
# print(orders_df.describe(include='all'))
# print('\n================================================\n')

customer_id_in_orders_df = orders_df.customer_id.tolist() # list customer who has order minimum once
customers_df['status'] = customers_df['customer_id'].apply(lambda x: 'Active' if x in customer_id_in_orders_df else 'Non Active') # categorize each customer who has order with status value is 'Active'
# print(customers_df.sample(5))

# print('\n================================================\n')
# print(customers_df.groupby(by='status').customer_id.count())
# print('\n================================================\n')

orders_customers_df = pd.merge(
    left=orders_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)
# print(orders_customers_df.head())
# print('\n================================================\n')
# # find orders by city
# print(orders_customers_df.groupby(by='city').order_id.nunique().sort_values(ascending=False).reset_index().head())

# print('\n================================================\n')

# count orders by states
# print(orders_customers_df.groupby(by='state').order_id.nunique().sort_values(ascending=False))

# print('\n================================================\n')

# count orders by gender
# print(orders_customers_df.groupby(by='gender').order_id.nunique().sort_values(ascending=False))

# print('\n================================================\n')

# search orders by age, classify it, make a column named age_group
orders_customers_df['age_group'] = orders_customers_df.age.apply(lambda x: 'Youth' if x <= 24 else ('Senior' if x >= 64 else 'Adult'))

# show it
# print(orders_customers_df.groupby(by='age_group').order_id.nunique().sort_values(ascending=False))

# print('\n================================================\n')

# explore product_df and sales_df data
# print(products_df.describe(include='all'))
# print(sales_df.describe(include='all'))

# explore product_df with min and max prices
# print(products_df.sort_values(by='price', ascending=False))

# search products by type and name
# print(products_df.groupby(by='product_type').agg({
#         'product_id': 'nunique',
#         'quantity': 'sum',
#         'price': ['min', 'max']
#     })
# )
# print(
#     products_df.groupby(by='product_name').agg({
#         'product_id': 'nunique',
#         'quantity': 'sum',
#         'price': ['min', 'max']
#     })
# )

# how to find biggest sales products
sales_products_df = pd.merge(
    left=sales_df,
    right=products_df,
    how='left',
    left_on='product_id',
    right_on='product_id',
)
# print(sales_products_df.head())

# find sales quantity and total_price by product_type
# print(sales_products_df.groupby(by='product_type').agg({
#     'sales_id': 'nunique',
#     'quantity_x': 'sum',
#     'total_price': 'sum'
# }))

# find sales quantity and total_price by product_name and sort by total_price
# print(
#     sales_products_df.groupby(by='product_name').agg({
#         'sales_id': 'nunique',
#         'quantity_x': 'sum',
#         'total_price': 'sum'
#     }).sort_values(by='total_price', ascending=False)
# )

# explore data all_df
all_df = pd.merge(
    left = sales_products_df,
    right=orders_customers_df,
    how='left',
    left_on='order_id',
    right_on='order_id',  
)
# print(all_df.head())

# explore sales by state and product_type
# print(
#     all_df.groupby(by=['state', 'product_type']).agg({
#         'quantity_x': 'sum',
#         'total_price': 'sum'
#     }).sort_values(by='total_price', ascending=False)
# )

# explore sales product_type by gender and age_group
print(
    all_df.groupby(by=['gender', 'product_type']).agg({
        'quantity_x': 'sum',
        'total_price': 'sum'
    })
)
print(
    all_df.groupby(by=['age_group', 'product_type']).agg({
        'quantity_x': 'sum',
        'total_price': 'sum'
    })
)