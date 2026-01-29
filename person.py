import random

import pokemon
from pokemon import *
POKEMONS = [FirePokemon("Charmander"), WaterPokemon("Squirtle"), ElectricPokemon("Pikachu"), GrassPokemon("Bulbasaur"),
            FirePokemon("Charizard")]

NAMES = ["Arthur", "Chi", "Michael", "Luis", "Peter", "Gary"]
class Person:
    def __init__(self, name=None, collection=None, money = 100):
        if collection is None:
            collection = []
        if name:
            self.name = name
        else:
            self.name = random.choice(NAMES)
        self.money = money
        self.collection = collection

    def show_money(self):
        print("{}'s bank account: ${}".format(self, self.money))

    def make_money(self, amount, fair_amount, Pokemon):
        if amount is not None:
            self.money += amount
        else:
            self.money += fair_amount
        print("{} got ${}!".format(self, fair_amount))
        self.show_money()

    def __str__(self):
        return self.name

    def status(self):
        print("Name: {}\nRole: {}\nPokémons: {}".format(self.name, self.role, len(self.collection)))

    def show_collection(self):
        print("---- {}'s Collection ----".format(self.name))
        if self.collection:
            for index,pokemon in enumerate(self.collection):
                print("{} - {}".format(index+1, pokemon))
        else:
            print("No Pokémon captured yet.")

    def choose_pokemon(self):
        if self.collection:
            chosenPokemon = random.choice(self.collection)
            print(color.BOLD + "\n{}: ".format(self.name) + color.END + color.ITALIC + color.BOLD +
                  "{}".format(chosenPokemon.name) + color.END + color.ITALIC + ", I choose you!\n" + color.END)
            return chosenPokemon
        else:
            print("No pokemon captured yet.")

    def battle(self, target):
        print("{} initiated a battle against {}!\n".format(self.name, target))
        myPokemon = self.choose_pokemon()
        target.show_collection()
        enemyPokemon = target.choose_pokemon()

        if myPokemon and enemyPokemon:
            while (myPokemon.hp >= 0 and enemyPokemon.hp >= 0):
                myPokemon.battle_attack(enemyPokemon)
                enemyPokemon.battle_attack(myPokemon)

            if(myPokemon.hp >= 0):
                print("{} won the battle!".format(self))
                self.make_money(None, fair_amount=myPokemon.level * 100, Pokemon=myPokemon)
            else:
                print("{} won the battle!".format(target))
                target.make_money(None, fair_amount=myPokemon.level * 100, Pokemon=enemyPokemon)
        else:
            print("The battle can not happen")

class Player(Person):
    role = "Player"

    def capture(self, pokemon):
        self.collection.append(pokemon)
        print("{} was captured!".format(pokemon))

    def choose_pokemon(self):
        self.show_collection()
        if self.collection:
            while True:
                choice = input("Choose a pokemon: ")
                try:
                    choice = int(choice)
                    chosenPokemon = self.collection[choice-1]
                    print(color.BOLD + "\n{}: ".format(self.name) + color.END + color.RED + color.BOLD + color.ITALIC +
                          "{}".format(chosenPokemon.name) + color.END + color.ITALIC + ", I choose you!\n" + color.END)
                    return chosenPokemon
                except:
                    print("Please enter a valid choice.")


        else:
            print("There are no pokemon captured yet.")

    def explore(self):
        if random.random() <= 0.3:
            pk = random.choice(POKEMONS)
            print("A wild {} has appeared!".format(pk))

            choice = input("Choose a pokemon? (y/n) ")
            if choice == "y":
                if(random.random() >= 0.5):
                    self.capture(pk)
                else:
                    print("{} ran away...".format(pk))
        else:
            print("You haven't found any Pokémon")

class Enemy(Person):
    role = "Enemy"

    def __init__(self, name=None, collection=[]):
        if not collection:
            for i in range(5):
                pokemons = [FirePokemon("Charmander"), WaterPokemon("Squirtle"), ElectricPokemon("Pikachu"),
                            GrassPokemon("Bulbasaur"), FirePokemon("Charizard")]
                collection.append(random.choice(pokemons))

        super().__init__(name=name, collection=collection)