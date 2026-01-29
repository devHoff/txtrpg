import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   ITALIC = '\x1B[3m'
   END = '\033[0m'

class Pokemon:
    def __init__(self, species, name=None, level=None):
        self.species = species

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        self.attack = self.level * 5
        self.hp = self.level * 10

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
        target.hp -= self.attack
        print("{} lost {}hp".format(target, self.attack))

class FirePokemon(Pokemon):
    element = "Fire"
    def fire_attack(self, target):
        print("{} threw a fire ball at {}!".format(self, target))
        super().attack(target)

class WaterPokemon(Pokemon):
    element = "Water"
    def water_attack(self, target):
        print("{} shot a water beam at {}!".format(self, target))
        super().attack(target)

class ElectricPokemon(Pokemon):
    element = "Electric"
    def electric_attack(self, target):
        print("{} cast a lightning bolt at {}!".format(self, target))
        super().attack(target)

class GrassPokemon(Pokemon):
    element = "Grass"
    def grass_attack(self, target):
        print("{} shot a grass ball at {}!".format(self, target))
        super().attack(target)





