''' program to get largest number from list using function'''
def largest(a):
    len=a[0]
    for i in a:
        if i>len:
            len=i
    return len
print("the largest number from list is",largest([5,10,8,15]))

 