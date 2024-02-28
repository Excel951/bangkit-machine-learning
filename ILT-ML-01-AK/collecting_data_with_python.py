import pandas as pd

# Read csv
df1 = pd.read_csv('./Telco-Customer-Churn.csv')

# Read excel
df2 = pd.read_excel('./Telco-Customer-Churn.xlsx')

# Read parquet
df3 = pd.read_parquet('./Telco-Customer-Churn.gzip')

# Read html
df4 = pd.read_html('./Telco-Customer-Churn.html')
df4 = df4[0]
print(df4)
df5 = df4.drop('UnnamedL 0', axis=1)
print(df5)