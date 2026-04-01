def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    new_string = ""
    return new_string.join(char for char in string_ if char not in vowels)