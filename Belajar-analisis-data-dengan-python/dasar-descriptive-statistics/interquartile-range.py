import numpy as np
from jumlah_kucing import jumlah_kucing

iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)
print(iqr)