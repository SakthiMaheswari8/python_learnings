''' this program is to find the value exist in given dictionary or not'''
keyword=input("enter the key word to find in list: ")
dict_1={"name":"liya","age":5}
if keyword in dict_1.values():
    print("value already exist")
else:
    print ("value is not there")
