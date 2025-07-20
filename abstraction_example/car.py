from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def printDetails(self):
        pass

    def accelerate(self):
        print("Speed up ...")

    def break_applied(self):
        print("Car stopped")

class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Not having this feature")

class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Available")

class Sedan(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Available in premium variants")

class Truck(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def load_capacity(self):
        print("Can carry up to 5000 kg")
