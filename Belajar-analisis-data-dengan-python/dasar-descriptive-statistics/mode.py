import numpy as np
from scipy import stats
from jumlah_kucing import jumlah_kucing

mode_jumlah_kucing = stats.mode(jumlah_kucing)[0]

print(mode_jumlah_kucing)