''' '''
class vote:
    def __init__(self):
        self.name=" "
        self.age=0
    def voter_name(self):
         self.name= input("enter your name: ")
    def voter_age(self):
        self.age= int(input("enter your age: "))
        try:
            if self.age>18:
                print(f"Hi {self.name} you are {self.age} so you are above 18 you are eligible to vote ")
            elif self.age<18:
                print(f"hi {self.name} you are {self.age} so you need to wait for {18-self.age} years to vote")
            else:
                print(f"hi {self.name} you are {self.age} you are just become eligible to vote")
        except ValueError:
            print("Error: Enter a valid number")
voter = vote()
voter.voter_name()
voter.voter_age()