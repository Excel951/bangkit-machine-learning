# how to write the csv file with dictionaries

import csv, os

def create_by_department_csv():
    users = [ 
        {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
        {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
        {"name": "Charlie Grey", "username": "greyc", "department": "Development"}
    ]
    keys = ["name", "username", "department"]

    with open("by_department.csv", "w") as by_department:
        writer = csv.DictWriter(by_department, fieldnames=keys)
        writer.writeheader()
        writer.writerows(users)
# create_by_department_csv()


# for software.csv and read_software_csv.py
def software_csv():
    softwares = [ 
        {"name": "MailTree", "version": "5.34", "status": "production", "users":"324"},
        {"name": "CalDoor", "version": "1.25.1", "status": "beta", "users":"22"},
        {"name": "Chatty Chicken", "version": "0.34", "status": "alphaa", "users":"4"}
    ]
    keys = ["name", "version", "status", "users"]
    
    with open("software.csv", "w") as software:
        writer = csv.DictWriter(software, fieldnames=keys)
        writer.writeheader()
        writer.writerows(softwares)
software_csv()