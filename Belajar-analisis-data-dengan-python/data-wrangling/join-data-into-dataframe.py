import pandas as pd

product_df = pd.read_csv("product.csv")
orders_df = pd.read_csv("orders.csv")

# how to joining data
# how => can be inner, left, right, and outer
# inner => merge all the data
# right => merge data from right side and the slices of two sides
# left => like right but from left side
# outer => take data only from the slices of two sides
new_order_df = pd.merge(
    left=product_df,
    right=orders_df,
    how="inner",
    left_on="product_id",
    right_on="product_id",
)