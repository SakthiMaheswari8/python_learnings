'''palindrom '''
def palindrom():
    a=input("enter a string:")
    b=a[::-1]
    print("the given string is:",a)
    if b == a:
        print("the given string is palindrome:",b)
    else:
        print("the given string is not a palindrome",b)
palindrom()
