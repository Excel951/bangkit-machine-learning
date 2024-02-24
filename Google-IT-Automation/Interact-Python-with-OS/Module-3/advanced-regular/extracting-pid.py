import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
if result is not None:
    print(result[1])
else:
    print(result)

result = re.search(regex, "A completely different string that also has numbers [34567]")
if result is not None:
    print(result[1])
else:
    print(result)

result = re.search(regex, "99 elephants in a [cage]")
# print(result[1])
# Note that this print command results in an error as shown in the video. 

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return "No pid found"
    return result[1]
print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))