import pandas as pd
import sqlalchemy as sqla

db = sqla.create_engine("sqlite:///mydata.sqlite")

# how to read table in database and present it in pandas DataFrame
pd.read_sql_table("table_name", db)

# how to read SQL query and present it in pandas DataFrame
pd.read_sql_query("SELECT * FROM table_name", db)

# how to read table or query in database and present it in pandas
pd.read_sql("SELECT * FROM table_name", db)