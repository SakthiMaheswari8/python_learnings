from car import Hatchback, Suv, Sedan, Truck

# Hatchback example
print("\n--- Hatchback Details ---")
car1 = Hatchback("Maruti", "Alto", "2022")
car1.printDetails()
car1.accelerate()
car1.sunroof()

# SUV example
print("\n--- SUV Details ---")
car2 = Suv("Hyundai", "Creta", "2023")
car2.printDetails()
car2.accelerate()
car2.sunroof()

# Sedan example
print("\n--- Sedan Details ---")
car3 = Sedan("Honda", "City", "2023")
car3.printDetails()
car3.accelerate()
car3.sunroof()

# Truck example
print("\n--- Truck Details ---")
car4 = Truck("Tata", "LPT 407", "2021")
car4.printDetails()
car4.accelerate()
car4.break_applied()
car4.load_capacity()
