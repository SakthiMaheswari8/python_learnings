'''arbitary argument function to find sum af given numbers'''
def sum_num(*num):
    tot=1
    for i in num:
        tot=tot+i
    print(tot)
sum_num(2,3,5)
