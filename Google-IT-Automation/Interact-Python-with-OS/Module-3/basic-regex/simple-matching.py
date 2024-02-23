import re

def search_pattern(pattern, word, ignore_case=False):
    if ignore_case:
        result = re.search(pattern, word, re.IGNORECASE)
    else:
        result = re.search(pattern, word)
    print(result)

# search_pattern(r"aza", "plaza")
# search_pattern(r"aza", "bazaar")
# search_pattern(r"aza", "maze")
# search_pattern(r"^x", "xenon")
# search_pattern(r"p.ng", "penguin")
# search_pattern(r"p.ng", "clapping")
# search_pattern(r"p.ng", "sponge")
# search_pattern(r"p.ng", "Pangaea", True)

def check_aei (text):
  result = re.search(r".a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True