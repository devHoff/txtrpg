import random

import pokemon
from pokemon import *
POKEMONS = [FirePokemon("Charmander"), WaterPokemon("Squirtle"), ElectricPokemon("Pikachu"), GrassPokemon("Bulbasaur"), FirePokemon("Charizard")]

NAMES = ["Arthur", "Chi", "Michael", "Luis", "Peter", "Gary"]
class Person:
    def __init__(self, name=None, collection=None):
        if collection is None:
            collection = []
        if name:
            self.name = name
        else:
            self.name = random.choice(NAMES)

        self.collection = collection

    def __str__(self):
        return self.name

    def status(self):
        print("Name: {}\nRole: {}\nPokémons: {}".format(self.name, self.role, len(self.collection)))

    def show_collection(self):
        print("---- {}'s Collection ----".format(self.name))
        if self.collection:
            for pokemon in self.collection:
                print("· {}".format(pokemon))
        else:
            print("No Pokémon captured yet.")

class Player(Person):
    role = "Player"

    def capture(self, pokemon):
        self.collection.append(pokemon)
        print("{} was captured!".format(pokemon))
class Enemy(Person):
    role = "Enemy"

    def __init__(self, name=None, collection=[]):
        if not collection:
            for i in range(5):
                pokemons = [FirePokemon("Charmander"), WaterPokemon("Squirtle"), ElectricPokemon("Pikachu"), GrassPokemon("Bulbasaur"), FirePokemon("Charizard")]
                collection.append(random.choice(pokemons))

        super().__init__(name=name, collection=collection)

#Player 1 created...
me = Player("John", POKEMONS)
rival = Enemy("Gary")


#Player status check
#me.status()

#Collection showcase
#me.show_collection()

rival.status()
rival.show_collection()

