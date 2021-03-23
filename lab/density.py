import requests as req
import json
import os.path
import os

pwd = os.path.dirname(os.path.realpath(__file__))
o = open(f"{pwd}/data/data.json")
data = json.load(o)
data = data["data"]

class Municipality:
    # EJERCICIO 11:
    total_density = 0
    #EJERCICIO 12:
    counter = 0
    #EJERCICIO 14:
    anual_growth = 1.02
    def __init__(self, name, density,area):
        self.name = name
        self.density = density
        self.area = area
        #EJERCICIO 11:
        Municipality.total_density += self.population
        #EJERCICIO 12:
        Municipality.counter += 1
    #EJERCICIO 8:
    def __str__(self):
        return f"{self.name}\n{self.density}\n{self.area}"

    #EJERCICIO 10:
    @property
    def population(self):
        return round(self.density * self.area, 2)

    #EJERCIO 13:
    @classmethod
    def from_str(cls, given_String):
        name, density, area = given_String.split("-")
        try:
            density = float(density)
            area = float(area)
        except TypeError as e:
            print("That's not a number, error: ", e)
        return cls(name, density, area)

    #EJERCICIO 15:
    def aply_anual_growth(self):
        return self.population * Municipality.anual_growth
    
    @staticmethod
    def num_of_countries(num):
        if num == 194:
            return True
        else:
            return False        
# EJERCICIO 7:
def create_Municipality(municipality):
    name = municipality["municipio_nombre"]
    density = municipality["densidad_por_km2"]
    area = municipality["superficie_km2"]

    return Municipality(name, density, area)

# EJERCICIO 9:
def all_to_objects(municipalities):
    return [create_Municipality(municipality) for municipality in municipalities]

#TESTS:
#7
ej7 = create_Municipality(data[0])
# print(ej7)
#8
# print(ej7)
#9
ej9 = all_to_objects(data)
print(Municipality.num_of_countries(10))
# print(ej9[0]) 
# 10
# print(ej7.population)
# 11
# print(Municipality.total_density)
# 13
ej13 = Municipality.from_str("test-116-12")
# print(ej13)
# 15
# print(ej7.aply_anual_growth())
o.close()
