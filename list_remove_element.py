'''This program is to remove the 0th,4th and 5th element from the list'''
list_1=[4,9,2,7,6,1,5,3]
for i in sorted([0,4,5],reverse=True):
    list_1.pop(i)
    list_1.append(list_1)
print(list_1)
