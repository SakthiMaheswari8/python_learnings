'''remove duplicates from list using function '''
def remove_duplicate(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b
print(remove_duplicate([1,5,4,1,5]))


 
