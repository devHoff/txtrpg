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

starter(Player("Arthur"))