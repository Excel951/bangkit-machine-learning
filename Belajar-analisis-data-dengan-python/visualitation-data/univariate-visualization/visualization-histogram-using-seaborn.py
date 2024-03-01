import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.random.normal(15, 5, 250)

# sns.histplot(x=x, bins=15)
# add kde to easily identify distributions of data quantitative
sns.histplot(x=x, bins=15, kde=True)
plt.show()