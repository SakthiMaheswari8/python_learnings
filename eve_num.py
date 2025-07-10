'''even number from the list'''
def even_num(a):
    for i in a:
        if i%2==0:
            print("the even number is",i)
        else:
            print("no even number")
even_num([5,5,5])