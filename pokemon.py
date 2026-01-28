class Pokemon:
    def __init__(self, name, element):
        self.name = name
        self.element = element
        print("Pokemon initialized")
        print("Name: " + name)
        print("Element: " + element)
        print("")

my_pokemon = Pokemon("Charmander", "Fire")
rivals_pokemon = Pokemon("Squirtle", "Water")