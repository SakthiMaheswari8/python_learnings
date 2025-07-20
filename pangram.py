'''This program is to find whether thr given string is pangram or not '''
import string
def pangram():
    b = a.lower()
    alphabet = set(string.ascii_lowercase)
    if alphabet.issubset(b):
        return "The given string is a pangram"
    else:
        return "The given string is not a pangram"
a=input("Enter the sentence to find whether the given is pangram or not:\n")
print(pangram())

    
    
    
 

