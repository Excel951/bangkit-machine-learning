import csv
import os

filename = open("csv_fle.txt", 'w')
csv_f = csv.reader(filename)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))