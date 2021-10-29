# Course: CS 30
# Period: 3
# Date created: Ocotober 20th, 2021
# Date modified: October 26th, 2021
# Name: Zana Osman
# Description: Character Selection and function for Text Based Adventure

# chrselect makes false until true
chrselect = True

# Characters with description
character_selection = ["Wonder Boy [1]", "Beefy Man [2]"]
character_s = {
    "Wonder Boy":
        {"Description": "A ninja raised in the forest who "
            "chases bears in his spare time",
            "Bonuses": "Has +3 Speed and +2 Damage points"},
    "Beefy Man":
        {"Description": "Average joe who might have lifted "
            "a little too much weights",
            "Bonuses": "Has +1 Damage and +4 Defense points"}
            }


def character_choice():
    '''Function to write out characters plus a mini description'''
    for character in character_s:
        print(f"\n{character}")
        for item in character_s[character]:
            print(f"{item} - {character_s[character][item]}")


def character_selected():
    '''Function to allow user to choose charater'''
    print("\nCharacters:")
    global chrselect
    character_choice()
    character_chosen = input("\nWhich character will you choose?\n")
    if character_chosen == "Wonder Boy":
        print("\nWonder Boy 'SELECTED'")
        print("Great choice, Extra speed will be on your side\n")
        chrselect = False
    elif character_chosen == "Beefy Man":
        print("\nBeefy Man 'SELECTED'")
        print("Excellent, Defense bonuses will come in handy\n")
        chrselect = False
    else:
        print("Maybe try to actually print a characters name correctly")
