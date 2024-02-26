# !C:\Python39\ python3

import sys

for line in sys.stdin:
    print(line.strip().capitalize())
    
# how to run this script
# using command in the bash like this:
# cat haiku.txt | python capitalize.py
# or
# python capitalize.py < haiku.txt
