import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# FROM EXPLORATORY DATA ANALYSIS
# =================================================================
delivery_time = orders_df["delivery_date"] - orders_df["order_date"] # initialize delivery_time with delivery_date - order_date
delivery_time = delivery_time.apply(lambda x: x.total_seconds()) # operation to each element in column of DataFrame or Series
orders_df["delivery_time"] = round(delivery_time/86400) # set delivery_time (day) in DataFrame

customer_id_in_orders_df = orders_df.customer_id.tolist() # list customer who has order minimum once
customers_df['status'] = customers_df['customer_id'].apply(lambda x: 'Active' if x in customer_id_in_orders_df else 'Non Active') # categorize each customer who has order with status value is 'Active'

orders_customers_df = pd.merge(
    left=orders_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)

# search orders by age, classify it, make a column named age_group
orders_customers_df['age_group'] = orders_customers_df.age.apply(lambda x: 'Youth' if x <= 24 else ('Senior' if x >= 64 else 'Adult'))

# how to find biggest sales products
sales_products_df = pd.merge(
    left=sales_df,
    right=products_df,
    how='left',
    left_on='product_id',
    right_on='product_id',
)

# explore data all_df
all_df = pd.merge(
    left = sales_products_df,
    right=orders_customers_df,
    how='left',
    left_on='order_id',
    right_on='order_id',  
)
# =================================================================

# VISUALIZATION DATA
# =================================================================
monthly_orders_df = all_df.resample(rule='M', on='order_date').agg({
    'order_id': 'nunique',
    'total_price': 'sum'
})

# used to format dates into YYYY-DD format
# monthly_orders_df.index = monthly_orders_df.index.strftime('%Y-%m')

# used to format dates into MM format
monthly_orders_df.index = monthly_orders_df.index.strftime('%B')

monthly_orders_df = monthly_orders_df.reset_index()
monthly_orders_df.rename(columns={
    'order_id': 'order_count',
    'total_price': 'revenue'
}, inplace=True)

# plt.figure(figsize=(10, 5))
# how to initialize line charts for Number of Orders per Month
# plt.plot(monthly_orders_df['order_date'], monthly_orders_df['order_count'], marker='o', linewidth=2, color='#72BCD4')
# plt.title('Number of Orders per Month (2021)', loc='center', fontsize=20)

# how to initialize line charts for Total Revenue per Month
# plt.plot(monthly_orders_df['order_date'], monthly_orders_df['revenue'], marker='o', linewidth=2, color='#72BCD4')
# plt.title('Total Revenue per Month (2021)', loc='center', fontsize=20)

# how to know wich the most products ordered
# sum_order_items_df = all_df.groupby('product_name').quantity_x.sum().sort_values(ascending=False).reset_index()

# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

# colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# sns.barplot(x='quantity_x', y='product_name', data=sum_order_items_df.head(5), palette=colors, ax=ax[0])
# ax[0].set_ylabel(None)
# ax[0].set_xlabel(None)
# ax[0].set_title("Best Performing Product", loc="center", fontsize=15)
# ax[0].tick_params(axis ='y', labelsize=12)

# sns.barplot(x="quantity_x", y="product_name", data=sum_order_items_df.sort_values(by="quantity_x", ascending=True).head(5), palette=colors, ax=ax[1])
# ax[1].set_ylabel(None)
# ax[1].set_xlabel(None)
# ax[1].invert_xaxis()
# ax[1].yaxis.set_label_position("right")
# ax[1].yaxis.tick_right()
# ax[1].set_title("Worst Performing Product", loc="center", fontsize=15)
# ax[1].tick_params(axis='y', labelsize=12)

# plt.suptitle("Best and Worst Performing Product by Number of Sales", fontsize=20)

# how to know demographic of customers
# by gender
# bygender_df = all_df.groupby(by="gender").customer_id.nunique().reset_index()
# bygender_df.rename(columns={
#     "customer_id": "customer_count"
# }, inplace=True)

# plt.figure(figsize=(10, 5))

# sns.barplot(
#     y="customer_count",
#     x="gender",
#     data=bygender_df.sort_values(by="customer_count", ascending=False),
#     palette=colors
# )
# plt.title("Number of Customer by Gender", loc="center", fontsize=15)

# by age
# byage_df = all_df.groupby(by="age_group").customer_id.nunique().reset_index()
# byage_df.rename(columns={
#     'customer_id': "customer_count"
# }, inplace=True)
# byage_df['age_group'] = pd.Categorical(byage_df['age_group'], ['Youth', 'Adults', 'Seniors'])
# plt.figure(figsize=(10, 5))
# colors_ = ["#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# sns.barplot(
#     y='customer_count',
#     x='age_group',
#     data=byage_df.sort_values(by='age_group', ascending=False),
#     palette=colors_
# )
# plt.title("Number of Customer by Age", loc="center", fontsize=15)

# plt.ylabel(None)
# plt.xlabel(None)
# plt.tick_params(axis='x', labelsize=12)

# by states
# bystate_df = all_df.groupby(by='state').customer_id.nunique().reset_index()
# bystate_df.rename(columns={
#     'customer_id': 'customer_count',
# }, inplace=True)
# plt.figure(figsize=(10,5))
# colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
# sns.barplot(
#     x='customer_count',
#     y='state',
#     data=bystate_df.sort_values(by='customer_count', ascending=False),
#     palette=colors_
# )
# plt.title('Number of Customer by States', loc='center', fontsize=15)
# plt.ylabel(None)
# plt.xlabel(None)
# plt.tick_params(axis='y', labelsize=12)

# RFM Analysis
# RFM analysis is method that used to segmentation customers by 3 parameters:
# recency, frequency, monetary
rfm_df=all_df.groupby(by='customer_id', as_index=False).agg({
    'order_date': 'max', # take last order date
    'order_id': 'nunique', # count order
    'total_price': 'sum' # calculate sum revenue
})
rfm_df.columns = ['customer_id', 'max_order_timestamp', 'frequency', 'monetary']

# calculate last customer do transaction (day)
rfm_df['max_order_timestamp'] = rfm_df['max_order_timestamp'].dt.date
recent_date = orders_df['order_date'].dt.date.max()
rfm_df['recency'] = rfm_df['max_order_timestamp'].apply(lambda x: (recent_date - x).days)

rfm_df.drop('max_order_timestamp', axis=1, inplace=True)
# print(rfm_df.head())

# identify best customer byu frequency, monetary, and recency parameter
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))

colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]

sns.barplot(y='recency', x='customer_id', data=rfm_df.sort_values(by='recency', ascending=True).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("By Recency (days)", loc="center", fontsize=18)
ax[0].tick_params(axis ='x', labelsize=15)

sns.barplot(y="frequency", x="customer_id", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("By Frequency", loc="center", fontsize=18)
ax[1].tick_params(axis='x', labelsize=15)
 
sns.barplot(y="monetary", x="customer_id", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
ax[2].set_ylabel(None)
ax[2].set_xlabel(None)
ax[2].set_title("By Monetary", loc="center", fontsize=18)
ax[2].tick_params(axis='x', labelsize=15)
 
plt.suptitle("Best Customer Based on RFM Parameters (customer_id)", fontsize=20)

# plt.xticks(fontsize=10)
# plt.yticks(fontsize=10)
plt.show()