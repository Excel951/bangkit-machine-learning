import os

with open("spider.txt", "w") as file:
    file.write("Spider has eight legs.\n")
file.close()

print(os.path.getsize("spider.txt"))
# get size file
print(os.path.getmtime("spider.txt"))
# get timestamp file

import datetime

timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))
# give date and time where more ease for read

print(os.path.abspath("spider.txt"))
# take file name and turn into an absolute path
