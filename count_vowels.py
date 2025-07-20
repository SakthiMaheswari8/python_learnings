'''This script defines a function to count the number of vowels in a user-input string.
It converts the string to lowercase and checks for vowels (a, e, i, o, u). '''         
def vowels():
    b = input("Enter a string: ")
    b = b.lower()   
    count = 0
    for i in b:
        if i in 'aeiou':
            count += 1
    print("Number of vowels:", count)
vowels()
