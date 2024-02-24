import re

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# to this when you want word with 5 digit. this will include cropped words
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# to this when you want exactly word with 5 digit characters
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))

print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.findall(r"\w{5,}", "I really like strawberries"))
print(re.search(r"s\w{,20}", "I really like strawberries"))

# quiz in video
def long_words(text):
  pattern = r"\b[\w]{7,}\b"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []