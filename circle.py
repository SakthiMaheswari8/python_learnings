''' This program is to display the area and perimeter of the circle using class '''
import math
class circle:
    def __init__(self,radius):
        self.radius = radius
         
    def circle_area(self):
        print("area of circle",math.pi*(self.radius**2))
    def circle_perimeter(self):
        print("perimeter of circle",math.pi *2*self.radius)

radius = int(input("enter the radius of circle:"))
x = circle(radius)
x.circle_area()
x.circle_perimeter()