# how to move file from one directory to another directory
# using low-level os module

import os

# check to see if a directory named "test1" exists under current working directory
# if not, create a new directory
dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
    
# construct source and destination path
src_file = os.path.join(os.getcwd(), "spider.txt")
dest_file = os.path.join(os.getcwd(), "test1", "spider.txt")

# move the file from its original location to the destination
os.rename(src_file, dest_file)