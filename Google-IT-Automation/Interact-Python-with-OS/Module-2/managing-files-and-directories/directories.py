import os


print(os.getcwd())
# using to get the current working directory

# os.mkdir("isi nama directory baru")
# using to create new directory

# os.chdir("isi dengan nama directory yang ingin dituju")
# using to move to other directory

# os.rmdir("isi nama directory yang ingin dihapus")
# using to delete directory

# os.listdir("website")
# This code snippet returns a list of all the files and sub-directories in the website directory.

dir = "../managing-files-and-directories"
for name in os.listdir(dir):
    fullname=os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
