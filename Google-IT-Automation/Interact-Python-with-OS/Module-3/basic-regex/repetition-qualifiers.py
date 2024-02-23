import re

# def wildcard_match(pattern, line_words):
#     result = re.search(pattern, line_words)
#     print(result)

# wildcard_match(r"Py.*n", "Pygmalion")
# wildcard_match(r"Py.*n", "Python Programming")
# wildcard_match(r"Py[a-z]*n", "Python Programming")
# wildcard_match(r"Py[a-z]*n", "Pyn")

# # find pattern like o and l but it can multiplied
# wildcard_match(r"o+l+", "goldfish") # ol
# wildcard_match(r"o+l+", "woolly") # ooll
# wildcard_match(r"o+l+", "ooolllive") # ooolll
# wildcard_match(r"o+l+", "boil") # none

# # find pattern started with p or none
# wildcard_match(r"p?each", "To each their own") # each
# wildcard_match(r"p?each", "I like peaches") #peach
# wildcard_match(r"p?each", "I like teaches") #each

def repeating_letter_a(text):
  result = re.search(r"[Aa].*[Aa]", text)
  return result != None
#   return result


print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True