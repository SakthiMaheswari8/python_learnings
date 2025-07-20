''' This program is find area of rectangle using class'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 10)
print(f"Area: {rect.calculate_area()}")
print(f"Perimeter: {rect.calculate_perimeter()}")
