'''This program is to find largest number from list'''
list1= input("Enter items separated by commas: ")
my_list = list1.split()
d=list1[0]
for i in list1:
    if i > d:
        d=i
print("the largest number in given list",d)