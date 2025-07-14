'''this program is to multiply the given number using function '''
def mul_num(*a):
    mul=1
    for i in a:
        mul*=i
    print(mul)
mul_num(2,5,2)