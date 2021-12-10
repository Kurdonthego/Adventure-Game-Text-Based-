# Course: CS 30
# Period: 3
# Date created: Ocotober 19th, 2021
# Date modified: December 10th, 2021
# Name: Zana Osman
# Description: Map for the game
try:
    import Combat as C
    import sys
except ModuleNotFoundError:
    print("Import failed in Map")
else:
    print("All modules printed succefully, ' Map '")


def Map():
    print('''
         ___________________________________________
        |          |          |          |          |
        |   ???    |  Enemy   |  Enemy   |  Finish  |
        |__________|__________|__________|__________|
        |  Health  |
        |   Pad    |
        |__________|
        |          |
        |  Enemy   |
        |__________|
        |          |
        |  Start   |
        |__________|
    ''')


def Start():
    print("\nWelcome to the land of doom")
    print("Your mission is to defeat the boss, Ethos")
    print("Good luck and hopefully you can make it\n")


def Ending():
    print(
        "\nYou have defeated the main boss, Ethos and have clear out all the scum from this land, you have now been rewarded 100 golden coin, may they bring you fortune\n"
    )


def Movement_Func():
    print("Choose your moves wisely, otherwise it may cost your life")
    C.Starting.name
    C.Starting.description
    print("Use N, E, S, W to move around")
    North1 = input("\nWhich way will you go?\n")
    global move
    if North1 == "N":
        print("\nMoving North")
        C.CombatToEnemy1()
        C.CombatToPlayer()
        North2 = input("\nWill you countinue?\n")
        if North2 == "N":
            print("\nMoving North")
            C.WhenHealing()
            North3 = input("\nGood thing you healed up, where to next?\n")
            if North3 == "N":
                print("\nMoving North")
                print("Nothing to be found")
                East1 = input("\nWhere shall you go next?\n")
                if East1 == "E":
                    print("\nMoving East")
                    C.CombatToEnemy2()
                    C.CombatToPlayer2()
                    East2 = input("\nSecond attack and survived? Where now?\n")
                    if East2 == "E":
                        print("\nMoving East")
                        C.CombatToEnemy3()
                        C.CombatToPlayer3()
                        East3 = input("\nWhich  way will you go?\n")
                        if East3 == "E":
                            print("\nMoving East")                       
                            C.CombatToBoss()
                            C.CombatToPlayerB()
                            Ending()
                            sys.exit()
                        else:
                            print("Wrong Movement")
                    else:
                        print("Wrong Movement")
                else:
                    print("Wrong Movement")
            else:
                print("Wrong Movement")
        else:
            print("Wrong Movement")
    else:
        print("Wrong Movement")
