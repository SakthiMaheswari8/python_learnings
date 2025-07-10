''' This program is to find the common values from the list'''

def common_list(a,b):
    c=a[0]
    for c in a:
        if c in b:
            return True
        else:
            return False
print(common_list(a=[4,5,8],b=[2,7,9]))




