import re

def wildcard_match(pattern, line_words):
    result = re.search(pattern, line_words)
    print(result)

# wildcard_match(r"[Pp]ython", "Python")
# wildcard_match(r"[a-z]way", "The end of the highway")
# wildcard_match(r"[a-z]way", "What a way to go")
# wildcard_match("cloud[a-zA-Z0-9]", "cloudy")
# wildcard_match("cloud[a-zA-Z0-9]", "cloud9")
# wildcard_match(r"[^a-zA-Z]", "This is a sentence with spaces.")
# wildcard_match(r"[^a-zA-Z ]", "This is a sentence with spaces.")

# wildcard_match(r"cat|dog", "I like cats.")
# wildcard_match(r"cat|dog", "I love dogs!")
# wildcard_match(r"cat|dog", "I like both dogs and cats.")

# wildcard_match(r"cat|dog", "I like cats.")
# wildcard_match(r"cat|dog", "I love dogs!")
# wildcard_match(r"cat|dog", "I like both dogs and cats.")
# print(re.findall(r"cat|dog", "I like both dogs and cats."))

def check_punctuation (text):
    # You can use the first or last code
    # it's give the same result
    
    # [a-z] will give you the character inside the square brackets
    # but if ^ given i.e. [^a-z] will exclude the character inside the square brackets
#   result = re.search(r"[^\w\s]", text)
  result = re.search(r"[^a-zA-Z ]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False