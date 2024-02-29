import pandas as pd
from sample_data import customers as customers_df, products as products_df, sales as sales_df, orders as orders_df

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


print(customers_df.describe(include='all'))
print('\n================================================\n')
print(customers_df.groupby(by='gender').agg({
    'customer_id': 'nunique',
    'age': ['max', 'min', 'mean', 'std'],
}))
print('\n================================================\n')
print(customers_df.groupby(by='city').customer_id.nunique().sort_values(ascending=False))
print('\n================================================\n')
print(customers_df.groupby(by='state').customer_id.nunique().sort_values(ascending=False))
print('\n================================================\n')

delivery_time = orders_df["delivery_date"] - orders_df["order_date"]
delivery_time = delivery_time.apply(lambda x: x.total_seconds())
orders_df["delivery_time"] = round(delivery_time/86400)

print(orders_df.describe(include='all'))
print('\n================================================\n')

customer_id_in_orders_df = orders_df.customer_id.tolist()
customers_df['status'] = customers_df['customer_id'].apply(lambda x: 'Active' if x in customer_id_in_orders_df else 'Non Active')
print(customers_df.sample(5))

print('\n================================================\n')
print(customers_df.groupby(by='status').customer_id.count())

orders_customers_df = pd.merge(
    left=orders_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)
orders_customers_df.head()