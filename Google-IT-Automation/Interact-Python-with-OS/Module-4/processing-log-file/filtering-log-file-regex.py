import sys, re

# logfile = sys.argv[1]
# with open(logfile) as f:
#     for line in f:
#         print(line.strip())

# with open(logfile) as f:
#     for line in f:
#         # if "CRON" not in line then continue to another line
#         if "CRON" not in line:
#             continue
#         print(line.strip())
        
pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1])

with open(logfile) as f:
    for line in f:
        # if "CRON" not in line then continue to another line
        if "CRON" not in line:
            continue
        pattern = r"USER \((.+)\)$"
        result = re.search(pattern, line)
        print(result[1])