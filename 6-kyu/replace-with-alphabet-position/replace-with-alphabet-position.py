import string
def alphabet_position(text):
    alphabet = string.ascii_lowercase
    return " ".join(str(alphabet.find(char) + 1) for char in text.lower() if char in alphabet)