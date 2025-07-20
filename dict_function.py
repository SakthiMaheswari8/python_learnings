'''This script defines a function that accepts any number of keyword arguments 
and prints each key-value pair. '''
def datas(**data):
    for i,j in data.items():
        print(f"{i}:{j}")
datas(name="sakthi",mark=85)

     
