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
print("select your option \n"
      "1)Addition \n"
      "2)Subtract\n"
      "3)multiplication\n"
      "4)division\n")     
choice=input("enter your choice:")
a=int(input("Enter the value for a:"))
b=int(input("enter the value for b:"))
if choice=="1":
    print("Addition of number is:",add(a,b))
elif choice=="2":
    print("subtraction of number is:",sub(a,b))
elif choice=="3":
    print("multiplication of number is:",mul(a,b))
elif choice=="4":
    print("division of number is:",div(a,b))
else:
    print("invalid value")



