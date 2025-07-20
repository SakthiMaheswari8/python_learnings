''' 
class student:
    name="sakthi"
    age=22
#using get attribute
print(getattr(student,'name'))
print(getattr(student,'age'))
#
print(getattr(student,'department','value not available'))
#using dot notation
print(student.name)
#creating new attribute using set attribute
setattr(student,"gender","female")
print(getattr(student,'gender'))
#creating new attribute using set attribute
student.city="chennai"
print(student.city)
print(student.__dict__)
delattr(student,"city")
print(student.__dict__)
####

class student:
    name="sakthi"
    age="22"
#get
print(getattr(student,"name"))
print(student.age)
#set
setattr(student,"dep","cs")
print(student.dep)

student.gender="female"
print(student.gender)
#get
print(getattr(student,"subject","the attribute is not available"))

############
# Define a class named 'Car'
class Car:
    # The __init__ method is a special method (constructor) that initializes new objects
    def __init__(self, make, model, year):
        self.make = make  # Instance attribute
        self.model = model  # Instance attribute
        self.year = year  # Instance attribute

    # Define a method for the Car class
    def display_info(self):
        print(f"This is a {self.year} {self.make} {self.model}.")

# Create objects (instances) of the 'Car' class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2024)

# Access attributes of the objects
print(f"Car 1 make: {car1.make}")
print(f"Car 2 model: {car2.model}")

# Call methods of the objects
car1.display_info()
car2.display_info()

# Modify an attribute of an object
car1.year = 2023
car1.display_info()'''

'''class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
'''

''' 
class Library:
    def __init__(self, books):
        self.books = list(books)   

    def available_book(self):
        print(f"\n{len(self.books)} books available:")
        for b in self.books:
            print("*", b)
        print()

    def borrow_book(self, book):
        for b in self.books:
            if b.lower() == book.lower():
                self.books.remove(b)
                print("Book issued.\n")
                return
        print("The book is not available.\n")

    def return_book(self, book):
        entry = {book}
        if entry in self.books:
            self.books.append(book)
            print("Book returned\n")
        else:
            print("No record of you borrowing that book.\n")
        
class Student:
    def request_book(self):
        book = input("Name of the book you want to borrow: ")
        return book

    def return_book(self):
        book = input("Name of the book you want to return: ")
        return book

def main():
    titles = ["C", "C++", "Python", "Java"]
    lib = Library(titles)
    user = Student()
    print("Welcome to ABC Library")
    print("1. List of books\n2. Borrow book\n3. Return book\n4. Exit\n")
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Enter a number.\n")
            continue
        if choice == 1:
            lib.available_book()
        elif choice == 2:
            book = user.request_book()
            lib.borrow_book(book)
        elif choice == 3:
            book = user.return_book()
            lib.return_book(book)
        elif choice == 4:
            print("Thank You\n")
            break
        else:
            print("Invalid choice.\n")
if __name__ == "__main__":
    main()'''

''' 
class Library:
    def __init__(self, books):
        self.books = list(books)
        self.original_books = list(books)  

    def available_book(self):
        print(f"\n{len(self.books)} books available:")
        for b in self.books:
            print("*", b)
        print()

    def borrow_book(self, book):
        for b in self.books:
            if b.lower() == book.lower():
                self.books.remove(b)
                print("Book issued.\n")
                return
        print("The book is not available.\n")

    def return_book(self, book):   
        if book.title()  not in self.original_books:
            print("This book is not from our library.\n")
            return
        for b in self.books:
            if b.lower() == book.lower():
                print("This book is already in the library.\n")
                return
        self.books.append(book)
        print("Book returned. Thank you\n")


class Student:
    def request_book(self):
        return input("Name of the book you want to borrow: ")

    def return_book(self):
        return input("Name of the book you want to return: ")


def main():
    titles = ["C", "C++", "Python", "Java"]
    lib = Library(titles)
    user = Student()

    print("Welcome to ABC Library")
    print("1. List of books\n2. Borrow book\n3. Return book\n4. Exit\n")

    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Enter a number.\n")
            continue

        if choice == 1:
            lib.available_book()
        elif choice == 2:
            book = user.request_book()
            lib.borrow_book(book)
        elif choice == 3:
            book = user.return_book()
            lib.return_book(book)
        elif choice == 4:
            print("Thank You\n")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()'''
'''
import random
import string

class PasswordGenerator:
    def __init__(self, name, account_no):
        self.name = name
        self.account_no = account_no

    def lower_case(self):
        print("Random lowercase letter:", random.choice(string.ascii_lowercase))

    def upper_case(self):
        print("Random uppercase letter:", random.choice(string.ascii_uppercase))

    def digit(self):
        print("Random digit:", random.choice(string.digits))

    def special_characters(self):
        print("Random special character:", random.choice(string.punctuation))


def main():
    name = input("Enter your name: ")
    account_no = input("Enter your account number: ")
    generator = PasswordGenerator(name, account_no)

    while True:
        print("\nSelect your option:")
        print("1) Lower case letter")
        print("2) Upper case letter")
        print("3) Digit")
        print("4) Special character")
        print("5) Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Enter a number.\n")
            continue

        if choice == 1:
            generator.lower_case()
        elif choice == 2:
            generator.upper_case()
        elif choice == 3:
            generator.digit()
        elif choice == 4:
            generator.special_characters()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()'''
    
'''# Import required modules
from abc import ABC, abstractmethod

# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Create abstract method      
    @abstractmethod
    def printDetails(self):
        pass
  
    # Create concrete method
    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Car stopped")

# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)                                                                                                                                                                                                                                                       
  
    def sunroof(self):
        print("Available")

# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")

# Call methods
car1.printDetails()
car1.accelerate()
car1.sunroof()'''

'''from abc import ABC, abstractmethod
class car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def details(self):
        pass
    
class hatchback(car):
    def details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
class suv(car):
    def details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
print("hatchback details ")        
car1 = hatchback("Maruti", "Alto", "2022")
car1.details()
print("SUV Details")
car2 = suv("Hyundai", "Creta", "2023")
car2.details()'''
'''from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass  # Abstract property, must be implemented by subclasses

class Dog(Animal):
    @property
    def species(self):
        return "Canine"

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)'''
# Parent class
'''class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    def speak(self):
        pass  # Placeholder method to be overridden by child classes

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"  # Override the speak method

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())'''

'''from abc import ABC, abstractmethod
class Animal(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
class Sound(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal, Sound):
    @property
    def name(self):
        return "Dog"
    def make_sound(self):
        return "Bark"
class Cat(Animal, Sound):
    @property
    def name(self):
        return "Cat"
    def make_sound(self):
        return "Meow"
class Cow(Animal, Sound):
    @property
    def name(self):
        return "Cow"
    def make_sound(self):
        return "Moo"
def describe_animal(animal: Animal):
    print(f"{animal.name} makes sound: {animal.make_sound()}")
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    describe_animal(animal)'''

'''from abc import ABC, abstractmethod

class animal(ABC):
    @property
    @abstractmethod
    def animal_name(self):
        pass

class sound(ABC):
    @abstractmethod
    def animal_sound(self):
        pass

class dog(animal, sound):
    @property
    def animal_name(self):
        return "dog"
    def animal_sound(self):
        return "bark"

class cow(animal, sound):
    @property
    def animal_name(self):
        return "cow"
    def animal_sound(self):
        return "mooo"

class cat(animal, sound):
    @property
    def animal_name(self):
        return "cat"
    def animal_sound(self):
        return "meoww..."

def ani(animal_obj):
    print(f"{animal_obj.animal_name} sound is {animal_obj.animal_sound()}")  # ✅ fixed
animals = [dog(), cow(), cat()]
for a in animals:
    ani(a)'''
##############################################3
#vote
'''def eligible_to_vote():
    try:
        a=int(input("enter your age:"))
        b=18-a
        if a>18:
            print("you are eligible to vote")
        elif a<18:
            print(f"you need to wait for {b} years to vote")
    except ValueError:
        print("enter a valid integer")
eligible_to_vote()'''
#
'''def eligible_to_vote(a, b):
    if a > 18:
        print("You are eligible to vote")
    elif a < 18:
        print(f"You need to wait for {b} years to vote")
try:
    a = int(input("Enter your age: "))
    b = 18 - a
    eligible_to_vote(a, b)
except ValueError:
    print("enter a valid integer.")'''
    
#the init function calls itself
    
'''class practice:
    def __init__(self,age):
         self.age=age
    def name(abc):
        print("sakthi")
    def detail(abc):
        print(22,self.age)
c=practice()
c.name()'''

class vote:
    def __init__(self):
        self.name=" "
        self.age=0
    def voter_name(self):
         self.name= input("enter yopur name: ")
    def voter_age(self,c):
        self.age= int(input("enter your age: "))
        c=18-self.age
        try:
            if self.age>18:
                print(f"Hi {self.name} you are {self.age} so you are above 18 you are eligible to vote ")
            elif self.age<18:
                print(f"hi {self.name} you are {self.age} so you need to wait for {c} years to vote")
        except ValueError:
            print("Error: Enter a valid number")
voter = vote()
voter.voter_name()
voter.voter_age()
         
    
 
 

