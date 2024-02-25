usernames = {}
name = "good_user"
# parameters of get: 
# first parameter is key
# second parameter is the default value if key not available
# if key available the second parameter not used
usernames[name] = usernames.get(name, 0) + 1
print(usernames)
usernames[name] = usernames.get(name, 0) + 1
print(usernames)

import re, sys

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    for line in f:
        if "CRON" in line:
            continue
        pattern = r"USER \((\w+)\)"
        result = re.search(pattern, line)

        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
        
print(usernames)