import matplotlib.pyplot as plt

cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
          'Surakarta','Surabaya', 'Medan', 'Makassar')

populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409)

# how to initialize bar charts
plt.bar(x=cities, height=populations)
# if you want to change rotation of bar charts into horizontal
plt.barh(y=cities, width=populations)

# modify x in bar charts
# this modify the rotation of x
plt.xticks(rotation=45)

# presentation bar charts
plt.show()