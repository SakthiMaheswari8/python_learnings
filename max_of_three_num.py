'''python function to find maximum of three numbers'''
def maximum_num(a,b,c):
    print(max(a,b,c))
maximum_num(5,8,2)

''' maximum value '''
def maximum_num(a,b,c):
    if a>b and a>c:
        print("a is the maximum value",a)
    if b>a and b>c:
        print("b is the maximum value",b)  
    else:
        print("c is the maximum value",c)  
maximum_num(5,8,2)