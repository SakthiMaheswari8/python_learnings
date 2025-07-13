'''remove duplicates from list using function '''
def remove_duplicate(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b
print(remove_duplicate([1,5,4,1,5]))

''' '''
'''def remove_duplicate(**val):
    d=" "
    for i in val.values():
        if i not in val:
            d.append(i)
    return d
print(remove_duplicate(a=1,b=1,c=2))'''

 
