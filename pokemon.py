class Pokemon:
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def __str__(self):
        return "Name: {}\nElement: {}\n".format(self.name, self.element)

    def attack(self, target):
        print("{} attacked {}!".format(self.name, target.name))

my_pokemon = Pokemon("Charmander", "Fire")
print(my_pokemon)

rivals_pokemon = Pokemon("Squirtle", "Water")
print(rivals_pokemon)

my_pokemon.attack(rivals_pokemon)