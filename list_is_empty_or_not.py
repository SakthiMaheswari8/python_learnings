'''This program is to check the list is empty or not'''

list1= input("Enter items separated by commas: ")
my_list = list1.split(',')
if len(list1)==0:
    print("list is empty")
else:
    print("list is not empty")
