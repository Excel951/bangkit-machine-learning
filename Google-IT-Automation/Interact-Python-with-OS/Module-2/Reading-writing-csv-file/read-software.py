import csv, os

with open("./software.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("{} has {} users".format(row["name"], row["users"]))