''' '''
from abc import ABC, abstractmethod
class animal(ABC):
    @property
    @abstractmethod
    def animal_name(self):
        pass
class sound:
    @property
    @abstractmethod
    def animal_sound(self):
        pass
class dog(animal,sound):
    @property
    def animal_name(self):
        return "dog"
    def animal_sound(self):
        return "bark"
class cow(animal,sound):
    @property
    def animal_name(self):
        return "cow"
    def animal_sound(self):
        return "mooo"
class cat(animal,sound):
    @property
    def animal_name(self):
        return "cat"
    def animal_sound(self):
        return "meoww..."
def ani(animal_obj):
    print(f"{animal_obj.animal_name} sound is {animal_obj.animal_sound()}")  
animals = [dog(), cow(), cat()]
for a in animals:
    ani(a)

    


    
        