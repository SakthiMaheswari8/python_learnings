'''This program is to display the details of the students using class '''
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def biodata(self):
        print("my name is",self.name)
        print("my age is",self.age)
x1=student("liya","5")
x2=student("sariga","5")
x1.biodata()
x2.biodata()