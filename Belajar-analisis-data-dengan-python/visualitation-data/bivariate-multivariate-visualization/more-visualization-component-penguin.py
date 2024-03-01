import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://query1.finance.yahoo.com/v7/finance/download/BBCA.JK?period1=1644796800&period2=1676332800&interval=1d&events=history&includeAdjustedClose=true'
df = pd.read_csv(url)
df['Date'] = pd.to_datetime(df['Date'])

penguins = sns.load_dataset('penguins')

sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='species', style='species')
plt.xlabel('Body Mass (Gram)', size=15)
plt.ylabel('Flipper Length (Milimeter)', size=15)
plt.show()