class Pokemon:
    def __init__(self, species, element, level=1, name=None):
        self.species = species
        self.element = element
        self.level = level

        #If the Pokémon has no given name, then it is called by the species name (ex: Charmander)
        if name:
            self.name = name
        else:
            self.name = species

    def __str__(self):
        return "Name: {}\nElement: {}\nLevel: {}\n".format(self.name, self.element, self.level)

    def attack(self, target):
        print("{}({}) attacked {}({})!".format(self.name, self.level, target.species, target.level))

my_pokemon = Pokemon("Charmander", "Fire", name = "João")
print(my_pokemon)

rivals_pokemon = Pokemon("Squirtle", "Water")
print(rivals_pokemon)

my_pokemon.attack(rivals_pokemon)