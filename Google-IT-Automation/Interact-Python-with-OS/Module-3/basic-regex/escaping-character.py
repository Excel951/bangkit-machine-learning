import re

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

def check_character_groups(text):
  result = re.search(r"\w\ ", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False