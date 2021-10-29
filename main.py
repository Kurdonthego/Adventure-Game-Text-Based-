# Course: CS 30
# Period: 3
# Date created: September 10th, 2021
# Date modified: October 28th, 2021
# Name: Zana Osman
# Description: Main File for Text Based Adventure
try:
    import sys
    import inventory as inv
    import characters as char
    import gamemap as mmap
except ModuleNotFoundError:
    print("Error, import failed")
    print("Game ended")
    sys.exit()

# Starting function to create username for player
print("Text-Based Adventure Menu")
print("Welcome user_")
Username_ = input("What shall I call you? ")
print("Ok " + Username_ + " what would you like to do?")

# Actions and directions possible
possible_actions = ["[1] Attack", "[2] Inventory", "[3] Explore",
                    "[4] Map", "[5] Quit"]
possible_directions = ["North [1]", "East [2]", "South [3]", "West [4]"]

# Function to choose character
while char.chrselect:
    char.character_selected()

# While loop for menu to stay active, will not close unless 'quit' is chosen
while True:
    """Function for the menu"""
    for action in possible_actions:
        print(f" {action}")
    menu_c = str(input("\nWhat action would u like to choose? "))
    if menu_c == "1":
        print("Attacking!\n")
    elif menu_c == "2":
        print("\nInventory:")
        inv.start_inventory_fnct()
        inv_desc = input("\nShow descriptions? \nYes [1], No [2] ")
        if inv_desc == "1":
            inv.inventory_description()
        else:
            print("No problemo")
    elif menu_c == "3":
        for direction in possible_directions:
            print(f" {direction}")
        directions_chosen = str(input("What direction would you like to go? "))
        if directions_chosen == "1":
            print("Going North!")
        elif directions_chosen == "2":
            print("Going East!")
        elif directions_chosen == "3":
            print("Going South!")
        elif directions_chosen == "4":
            print("Going West!")
    elif menu_c == "4":
            print("World Map")
            mmap.print_map()
    # Quit function will work with the sys.exit command
    elif menu_c == "5":
        if menu_c == "5":
            choice_s = str(input("Are you sure you would like to exit? [1] "))
            if choice_s.lower() == "1":
                print("Exiting, Goodbye " + Username_)
                sys.exit()
        else:
            print("Countinue!")
    else:
        print("Sorry that does not work, Choose a different option ")
