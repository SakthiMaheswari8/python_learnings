''' '''
import string

def pangram():
    a = input("Enter the sentence to find whether the given is pangram or not:\n")
    b = a.lower()
    print(b)
    alphabet = set(string.ascii_lowercase)
    print(alphabet)
    i = 0
    while i < len(b):
        if b[i] in alphabet:
            alphabet.remove(b[i])
        i += 1
    if not  alphabet:
        return "The given string is a pangram"
    else:
        return "The given string is not a pangram"

print(pangram())