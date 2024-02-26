import re, csv

user_dict = {}
error_dict = {}

with open('./syslog.log', 'r') as f:
    for line in f:
        # pattern = r"(ERROR|INFO)\s*([\w*\s*\d*\[\]\#]*)\s*(\(\w*\d*\s*\.*\))"
        pattern = r"(ERROR|INFO)\s*([^\\]*)\s*(\(\w*\d*\s*\.*\))"
        result = re.search(pattern, line)
        if result is None:
            continue
        # print(result)
        
        log_type = result[1]
        message = result[2]
        username = result[3]
        
        print(log_type, message, username)
        
        if log_type.lower() == 'error':
            if message not in error_dict:
                error_dict[message] = 0
            error_dict[message] += 1
            
        if username not in user_dict:
            user_dict[username] = {'error': 0, 'info': 0}
        user_dict[username][log_type.lower()] += 1
        
sorted_error_dict = [("Error", "Count")]+sorted(error_dict.items(), key=lambda x: x[1], reverse=True)
sorted_user_dict = sorted(user_dict.items(), key=lambda x: x[0], reverse=True)

with open('error_message.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sorted_error_dict)
    
with open('user_statistics.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows([(user, stats['info'], stats['error']) for user, stats in sorted_user_dict])
