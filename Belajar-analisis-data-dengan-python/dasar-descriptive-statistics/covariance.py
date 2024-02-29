import pandas as pd
from sample_data import sample_data

df = pd.DataFrame(sample_data)

print(df.cov(numeric_only=True))