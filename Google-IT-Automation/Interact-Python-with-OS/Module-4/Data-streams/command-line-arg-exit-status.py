import sys

# how to run file with argument value
# py name_file.py argument1 argument2 argument3 etc.
# i.e. py command-line-arg-exit-status.py coba-argv

print(sys.argv)

import os

filename = './'+sys.argv[1]

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists".format(filename))
    sys.exit(1)
    
