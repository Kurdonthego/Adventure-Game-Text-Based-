# Course: CS 30
# Period: 3
# Date created: December 6th, 2021
# Date modified: December 10th, 2021
# Name: Zana Osman
# Description: Inventory for Text Based Adventure


class Weapon():
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

    def __str__(self):
        return str(self.name) + " : " + str(self.description)


Knife = Weapon('Knife', 'Capable of dealing 5 damage', 5)


def Inventory():
    print(Knife)
