def character_frequency(filename):
    # counts the frequency of each characters in the given file.
    try:
        f = open(filename)
    except OSError:
        return None
    
    # Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters