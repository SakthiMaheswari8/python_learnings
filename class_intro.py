''' This script defines a Person class that stores name, age, and department 
information, and prints a greeting using the provided data. '''
class Person:
  def __init__(self, name, age,dept):
    self.name = name
    self.age = age
    self.dept= dept

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("Hello my age is " , self.age)
    print("Hello my dept is " + self.dept)

p1 = Person("raghul", 36,"IT")
p1.myfunc()