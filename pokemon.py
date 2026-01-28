import random

class Pokemon:
    def __init__(self, species, name=None, level=None):
        self.species = species

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        #If the Pokémon has no given name, then it is called by the species name (ex: Charmander)
        if name:
            self.name = name
        else:
            self.name = species

    def __str__(self):
        return "{}({})".format(self.name, self.level)

    def status(self):
        print("Name: {}\nElement: {}\nLevel: {}\n".format(self.name, self.element, self.level))

    def attack(self, target):
        print("{} attacked {}!".format(self, target))

class FirePokemon(Pokemon):
    element = "Fire"
    def fire_attack(self, target):
        print("{} threw a fire ball at {}!".format(self, target))

class WaterPokemon(Pokemon):
    element = "Water"
    def water_attack(self, target):
        print("{} shot a water beam at {}!".format(self, target))

class ElectricPokemon(Pokemon):
    element = "Electric"
    def electric_attack(self, target):
        print("{} cast a lightning bolt at {}!".format(self, target))

class GrassPokemon(Pokemon):
    element = "Grass"
    def grass_attack(self, target):
        print("{} shot a grass ball at {}!".format(self, target))





