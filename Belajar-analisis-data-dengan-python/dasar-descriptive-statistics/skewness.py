# used for measuring simetric of data distribution
# plus value skewness for right skewed
# zero value skewness for perfect simetric
# minus value skewness for left skewed

import numpy as np
import pandas as pd
from jumlah_kucing import jumlah_kucing

jumlah_kucing_series = pd.Series(jumlah_kucing)
print(jumlah_kucing_series.skew())