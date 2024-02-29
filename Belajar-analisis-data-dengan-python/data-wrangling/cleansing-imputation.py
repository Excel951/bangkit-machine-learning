# this method working to fill missing values
import pandas as pd

data = pd.read_csv('employee_data.csv')

data.age.fillna(value=data.age.mean(), inplace=True)