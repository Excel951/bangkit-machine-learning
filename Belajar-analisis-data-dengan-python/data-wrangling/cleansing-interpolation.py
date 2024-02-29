# Metode penanganan missing value terakhir yang akan kita bahas ialah interpolation (interpolasi).
# Sederhananya, interpolasi merupakan salah satu pendekatan numerik yang digunakan untuk
# menghitung titik data baru berdasarkan range data yang sudah ada.
# Perhitungan ini menggunakan sebuah persamaan garis linear ataupun polynomial.
# Perhitungan tersebut membuat metode ini sangat cocok digunakan untuk menangani
# missing value pada data time series.

# Library pandas juga menyediakan method interpolate() yang bisa kita gunakan untuk menerapkan
# metode interpolasi dalam mengatasi missing value.
# Ketika menggunakan method ini, kita perlu mendefinisikan metode interpolasi yang ingin digunakan,
# seperti linear, polynomial, dll. Selain itu, kita juga perlu mendefinisikan
# parameter limit_direction (forward, backward, dan both) untuk menspesifikkan arah konstruktif
# dari proses interpolasi. Berikut merupakan contoh kode untuk menggunakan method interpolate().

import pandas as pd

data = pd.read_csv('bbca_index.csv')

data.close_price.interpolate(method='linear', limit_direction='forward', inplace=True)