'''random number generation 
import random
a=int(input("enter a random number to guess from (1 to 100): "))
b=random.randint(1,100)
if a==b:
    print("you gussed the correct number")
else:
    print("the gussed number is wrong")
print("the random number genrated by the the system is:",b)'''

#
import random

# Introduction
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate random number
secret_number = random.randint(1, 100)

# Initialize variables
guess = None
attempts = 0

# Game loop
while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
    except ValueError:
        print("Please enter a valid integer.")

