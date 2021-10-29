# Course: CS 30
# Period: 3
# Date created: Ocotober 19th, 2021
# Date modified: October 28th, 2021
# Name: Zana Osman
# Description: Map for the game
try:
    import sys
    from tabulate import tabulate
except ModuleNotFoundError:
    print("Error, import failed")
    print("Game ended")
    sys.exit()

game_map = ('''
_________________________________________________________________________
|                 |    Cracking     |     Enemy       |      Space      |
|                 |     Canyon      |     Tile        |     Station     |
|_________________|_________________|_________________|_________________|
|    Northton     |      Boss       |    Roaring      |                 |
|                 |     Battle      |    Rivers       |                 |
|_________________|_________________|_________________|_________________|
|     Enemy       |                 |     Tilting     |      Boss       |
|     Tile        |                 |      Town       |     Battle      |
|_________________|_________________|_________________|_________________|
|      Boss       |    Sneaky       |                 |      Safe       |
|     Battle      |    Suburbs      |                 |      House      |
|_________________|_________________|_________________|_________________|
|   Destruction   |                 |      Enemy      |       East      |
|     Diner       |                 |      Tile       |    Extraction   |
|_________________|_________________|_________________|_________________|
|                 |      Drop       |                 |     Crashed     |
|                 |      Zone       |                 |     Cruizer     |
|_________________|_________________|_________________|_________________|
   ''')

world_map = [
            ["  ", "CC", "ET", "SS"],
            ["NT", "BB", "RR", "  "],
            ["ET", "  ", "TT", "BB"],
            ["BB", "SB", "  ", "SH"],
            ["DD", "  ", "ET", "EE"],
            ["  ", "DZ", "  ", "CZ"]
]

map_tiles = {
    "Cracking Canyon":
        {"description": "One wrong step could mean the end",
            "abbreviation": "CC",
            "requirement": "Rope"},
    "Space Station":
        {"description": "Station with advanced tech",
            "abbreviation": "SS",
            "requirement": "none"},
    "Northton":
        {"description": "Tent town, may have a few weapons left behind",
            "abbreviation": "NT",
            "requirement": "none"},
    "Roaring Rivers":
        {"description": "One way path through the roaring  river",
            "abbreviation": "RR",
            "requirement": "none"},
    "Tilting Town":
        {"description": "One way path through the roaring  river",
            "abbreviation": "TT",
            "requirement": "Heavy Boots"},
    "Sneaky Suburbs":
        {"description": "Quiet neighborhood with a little too much trouble",
            "abbreviation": "SB",
            "requirement": "none"},
    "Destruction Diner":
        {"description": "Just a diner in the middle of nowhere,"
                        " may have supplies",
            "abbreviation": "DD",
            "requirement": "none"},
    "East Extraction":
        {"description": "Military extractio, may have military grade weapons",
            "abbreviation": "EE",
            "requirement": "none"},
    "Drop Zone":
        {"description": "Supply drop could mean extra weapons",
            "abbreviation": "DZ",
            "requirement": "Flare Gun"},
    "Crashed Cruizer ":
        {"description": "Crashed space cruizer, potential bandits in area",
            "abbreviation": "CZ",
            "requirement": "none"},
    "Enemy Tile":
        {"description": "Possible enemy on tile, might even be multiple",
            "abbreviation": "ET",
            "requirement": "none"},
    "Boss Battle":
        {"description": "Boss inbound, may want to reconsider choices",
            "abbreviation": "BB",
            "requirement": "none"},
    "Safe House":
        {"description": "Safe house to rest and heal up!",
            "abbreviation": "SH",
            "requirement": "key"}
             }


def array_map():
    '''Prints map into an organized array'''
    print(tabulate(world_map, tablefmt='plain'))


def gmap_fnc():
    '''Prints out locations with descriptions'''
    for location in map_tiles:
        print(f"\n{location}:")
        for item in map_tiles[location]:
            print(f"{item} - {map_tiles[location][item]}")


def print_map():
    '''Prints world map'''
    print(game_map)
    array_map()
    gmap_fnc()
