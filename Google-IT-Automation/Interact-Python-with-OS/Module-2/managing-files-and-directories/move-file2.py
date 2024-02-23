# how to move a file to a different location
# using Pathlib

from pathlib import Path

# check if the directory named "test1" exists
# if not, create one
dest_dir = Path("./test1")
if not Path.exists(dest_dir):
    dest_dir.mkdir()
    
# construct sorce and destination directories
src_file = Path("./spider.txt")
dest_file = dest_dir/"spider.txt"

# move the file to destination directory
if src_file.rename(dest_file):
    print("Moving successfully!")
else:
    print("Failed to move!")