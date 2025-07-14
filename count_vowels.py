''' '''         
def vowels():
    b = input("Enter a string: ")
    b = b.lower()   
    count = 0
    for i in b:
        if i in 'aeiou':
            count += 1
    print("Number of vowels:", count)
vowels()
