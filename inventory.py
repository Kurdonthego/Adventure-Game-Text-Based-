# Inventory (Starting weapons)
inventory_s = {
    "Small Knife":
        {"Description": "Provides small damage and "
            "can be used for utilities", "Damage": 5, "Protection": 0},
    "Axe":
        {"Description": "Can cut down wooden and metal doors",
            "Damage": 15, "Protection": 0},
    "Shield":
        {"Description": "Provides protection against arrows,"
            " swords and bullets",
            "Damage": 0, "Protection": 20}
        }


# Function to only list name of weapons
def start_inventory_fnct():
    for weapon in inventory_s:
        print(f"{weapon}")


# Function to list name of weapons plus description
def inventory_description():
    for weapon in inventory_s:
        print(f"\n{weapon}:")
        for item in inventory_s[weapon]:
            print(f"{item} - {inventory_s[weapon][item]}")