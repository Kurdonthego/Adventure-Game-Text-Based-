# Course: CS 30
# Period: 3
# Date created: September 10th, 2021
# Date modified: December 10th, 2021
# Name: Zana Osman
# Description: Main File for Text Based Adventure
try:
    import sys
    import Map as M
    import Inventory as Inv
except ModuleNotFoundError:
    print("Error, import failed in MainFile")
    print("Game ended")
    sys.exit()
else:
    print("All modules printed succefully, ' MainFile '")


# Starting function that will introduce player to game
M.Start()


# Actions and directions possible
possible_actions = [
    "For Movement Type 'F'", "For Inventory Type 'I'",
    "For Statistics Type 'S'", "For Map Type 'M'", "For Quit Type 'Q'"
]

# While loop for menu to stay active, will not close unless 'quit' is chosen
while True:
    """Function for the menu"""
    for action in possible_actions:
        print(f" {action}")
    menu_c = str(input("\nWhat action would u like to choose? \n"))
    if menu_c == "I":
        print("\nCurrent Inventory:")
        Inv.Inventory()
    elif menu_c == "F":
        M.Movement_Func()
    elif menu_c == "S":
        print("Ethans big black cock")
    elif menu_c == "M":
        print("\nMap:")
        M.Map()
    # Quit function will work with the sys.exit command
    elif menu_c == "Q":
        if menu_c == "Q":
            choice_s = str(
                input("\nAre you sure you would like to exit? [Y] "))
            if choice_s == "Y":
                print("Exiting, Goodbye")
                sys.exit()
        else:
            print("Countinue!")
    else:
        print("\nSorry that does not work, Choose a different option\n")
