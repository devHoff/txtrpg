from pokemon import *

class Person:
    def __init__(self, name=None, collection = []):
        if name:
            self.name = name
        else:
            self.name = "..."

        self.collection = collection

    def status(self):
        print("Name: {}\nRole: {}\nPokémons: {}".format(self.name, self.role, len(self.collection)))

    def show_collection(self):
        print("---- {}'s Collection ----".format(self.name))
        for pokemon in self.collection:
            print("· {}".format(pokemon))

class Player(Person):
    role = "Player"

class Enemy(Person):
    role = "Enemy"

pk1 = FirePokemon("Charmander")
pk2 = WaterPokemon("Squirtle")
pk3 = ElectricPokemon("Pikachu")

me = Player("Arthur", [pk1, pk2, pk3])
me.status()
me.show_collection()