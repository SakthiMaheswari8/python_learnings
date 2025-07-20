''' '''
import string
import random
length = int(input("Enter password length: "))
print('''Choose character set for password from these : 
         1. letters
         2. lowercase letter
         3. uppercase letters
         4. digits
         5. Special characters
         6. Exit''')
characterList = ""
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
        characterList += string.ascii_letters
    elif (choice == 2):
        characterList += string.ascii_lowercase
    elif (choice == 3):
        characterList += string.ascii_lowercase
    elif(choice == 4):
        characterList += string.digits
    elif(choice == 5):
        characterList += string.punctuation
    elif(choice == 6):
        break
    else:
        print("Please pick a valid option!")
password = []
for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
print("The random password is " + "".join(password))