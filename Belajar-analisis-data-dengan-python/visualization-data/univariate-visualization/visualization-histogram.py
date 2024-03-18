# Parameter in hist()
# x : contain data that will be visualized
# bins : contain count of bins that will be used in the histogram

import matplotlib.pyplot as plt
import numpy as np

# generate random data with normal distribution
# data will generated 250 data points 
# with mean values is 15 and standard deviation values is 5
x = np.random.normal(15, 5, 250)

plt.hist(x=x, bins=15)
plt.show()