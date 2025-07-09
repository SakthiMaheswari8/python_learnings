'''this is the program to remove duplicate from list'''
num=[5,8,3,4,5,8]
print("list before removing duplicates: ",num)
b=[]
for i in num:
    if i not  in b:
        b.append(i)
print(b)
     
        