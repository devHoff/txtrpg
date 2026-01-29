import pickle

from person import *

def starter(player):
    print("Hey {}, choose a starter Pokémon to accompany you throughout your journey...\n".format(player))

    bulbasaur = GrassPokemon("Bulbasaur", level=1)
    charmander = FirePokemon("Charmander", level=1)
    squirtle = WaterPokemon("Squirtle", level=1)

    print("(1)", bulbasaur)
    print("(2)", charmander)
    print("(3)", squirtle)

    choice = None

    while True and (choice != "3" or choice != "1" or choice != "2"):
        choice = input("\nChoose (1, 2 or 3) ----> ")
        if choice == "1":
            player.capture(bulbasaur)
            break;
        elif choice == "2":
            player.capture(charmander)
            break;
        elif choice == "3":
            player.capture(squirtle)
            break;
        else:
            print("Choose only between 1 and 3.")

    print()
    player.show_collection()

player = Player("Arthur", [FirePokemon("Charizard", level=1)])
enemy1 = Enemy("Gary", [WaterPokemon("Squirtle", level=2)])

def save(player):
    try:
        with open("save.db", "wb") as f:
            pickle.dump(player, f)
            print("Game saved")
    except Exception as error:
        print("Could generate save file.")
        print(error)

def load_save():
    try:
        with open("save.db", "rb") as f:
            new_player = pickle.load(f)
        print("Game loaded")
        return new_player
    except Exception as error:
        print("Could not load game.")
        print(error)
        return None

if __name__ == "__main__":
    print("------------------")
    print("Welcome to Terminal POKEMÓN RPG")
    print("------------------")
    name = input("Enter your name: ")
    player = Player(name)
    print("Hello {}, this is a wolrd habited by Pokémons. From now on, your mission will be to"
          "become a Pokémon master!".format(player))
    print("Catch as much of them as you can!")
    player.show_money()

    if player.collection:
        print("I can see that you already have some Pokémons...")
        player.show_collection()
    else:
        print("You don't have any Pokémons yet, so you shall choose one.")
        starter(player)

    print("Great! Now that you already have a Pokémon, you shall fight your rival: Gary!")

    while True:
        print("------------------")
        print("Choose an action:")
        print("1 - Explore the world")
        print("2 - Fight an enemy")
        print("3 - Inspect collection")
        print("4 - Save game")
        print("5 - Load game")
        print("6 - Quit")
        choice = input("Choose (1, 2 or 3) ----> ")

        try:
            choice = int(choice)
        except:
            print("Please enter a valid choice.")

        if int(choice == 1):
            player.explore()
        elif choice == 2:
            enemy = Enemy()
            player.battle(enemy)
        elif choice == 3:
            player.show_collection()
        elif choice == 4:
            save(player)
        elif choice == 5:
            player = load_save()
        elif choice == 6:
            break

