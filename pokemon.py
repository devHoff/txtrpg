class Pokemon:
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def __str__(self):
        return "Name: " + self.name + "\nElement: " + self.element + "\n"


my_pokemon = Pokemon("Charmander", "Fire")
print(my_pokemon)

rivals_pokemon = Pokemon("Squirtle", "Water")
print(rivals_pokemon)