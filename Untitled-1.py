''''''
from abc import ABC, abstractmethod
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
car2.details()


    
