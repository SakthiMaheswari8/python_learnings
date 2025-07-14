'''simple calculater '''
 def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
<<<<<<< HEAD
while True:
=======
while (True):
>>>>>>> b5a2f1511fa81c7f2fb9acadd476a96790511194
    print("select your option \n"
      "1)Addition \n"
      "2)Subtract\n"
      "3)multiplication\n"
      "4)division\n"
<<<<<<< HEAD
      "5)exit\n")     
    choice=input("enter your choice:")
    a=int(input("Enter the value for a:"))
    b=int(input("enter the value for b:"))
=======
      "5)exit\n")  
    choice=input("enter your choice:")
    if choice=="5":
        print("thank you")
        break
    if choice in("1","2","3","4"):
        a=int(input("Enter the value for a:"))
        b=int(input("enter the value for b:")) 
>>>>>>> b5a2f1511fa81c7f2fb9acadd476a96790511194
    if choice=="1":
        print("Addition of number is:",add(a,b))
    elif choice=="2":
        print("subtraction of number is:",sub(a,b))
    elif choice=="3":
        print("multiplication of number is:",mul(a,b))
    elif choice=="4":
        print("division of number is:",div(a,b))
<<<<<<< HEAD
    elif choice=="5":
        print("thank you")
        break
=======
>>>>>>> b5a2f1511fa81c7f2fb9acadd476a96790511194
    else:
        print("invalid value")



