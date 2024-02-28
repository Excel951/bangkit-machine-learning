import numpy as np
import pandas as pd
from jumlah_kucing import jumlah_kucing

jumlah_kucing_series = pd.Series(jumlah_kucing)
print(jumlah_kucing_series.var())