# Course: CS 30
# Period: 3
# Date created: December 9th, 2021
# Date modified: December 10th, 2021
# Name: Zana Osman
# Description: Combat for the game
try:
    import Map as M
except ModuleNotFoundError:
    print("Import failed in Map")
else:
    print("All modules printed succefully, ' Combat '")


# Hero Class
class Hero():
    def __init__(self, name, description, health, attack):
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack


# Hero
TheNeutralizer = Hero('The Neutralizer', 'Demon with extra health', 200, 150)


# Base Tile class
class Tile():
    def __init__(self, name, description):
        self.name = name
        self.description = description


# Enemy tile class
class Enemy(Tile):
    def __init__(self, name, description, health, damage):
        super().__init__(name, description)
        self.health = health
        self.damage = damage


# All Enemy
Omar = Enemy("Omar", "Zombie with accelerated health", 30, 10)

Shaman = Enemy("Shaman", "Shaman with extra damage", 15, 20)

MiniBoss = Enemy("Mini Boss", "Big boy mini boss", 100, 50)

Boss = Enemy("Ethos", "Biggest, baddest, boss", 50, 20)


# Starting Tile Function
class StartingTile(Tile):
    def __init__(self, name, description):
        super().__init__(name, description)


Starting = StartingTile(
    "Starting",
    "Welcome to the start of your adventure where your mission" +
    "is to slay the boss, Ethos"
)


class HealthGainTile(Tile):
    def __init__(self, name, description, health):
        super().__init__(name, description)
        self.health = health


HealUp = HealthGainTile("Heal", "Heal up for added health, you may need it",
                        10)


class FinishingTile(Tile):
    def __init__(self, name, description):
        super().__init__(name, description)


Finish = FinishingTile(
    "Finish", "You have succesfully defeated the boss and have won the game")


# First Combat set, tile x = 1, y = 2
def CombatToEnemy1():
    Omar.health = Omar.health - TheNeutralizer.attack
    if Omar.health <= 0:
        print('Omar Health: ' + str(Omar.health))
        print("You have killed the enemy, hopefully you last until the next")

    else:
        print("The enemy has not been slain")


def CombatToPlayer():
    TheNeutralizer.health = TheNeutralizer.health - Omar.damage
    if TheNeutralizer.health >= 0:
        print(TheNeutralizer.health)
        print(
            "So you have survived the first attack?" +
            "Will you be able to last until the next?"
        )

    else:
        print("You have perished")


# Second Combat set, tile x = 2, y = 4
def CombatToEnemy2():
    Shaman.health = Shaman.health - TheNeutralizer.attack
    if Shaman.health <= 0:
        print('Shaman Health: ' + str(Shaman.health))
        print("You have killed the enemy, hopefully you last until the next")

    else:
        print("The enemy has not been slain")


def CombatToPlayer2():
    TheNeutralizer.health = TheNeutralizer.health - Shaman.damage
    if TheNeutralizer.health >= 0:
        print(TheNeutralizer.health)
        print("Glad you made it through yet another, countinue on")

    else:
        print("You have perished")


# Third Combat set, tile x = 3, y = 4
def CombatToEnemy3():
    MiniBoss.health = MiniBoss.health - TheNeutralizer.attack
    if MiniBoss.health <= 0:
        print('Mini Boss Health: ' + str(MiniBoss.health))
        print("You have killed the enemy, hopefully you last until the next")

    else:
        print("The enemy has not been slain")


def CombatToPlayer3():
    TheNeutralizer.health = TheNeutralizer.health - MiniBoss.damage
    if TheNeutralizer.health >= 0:
        print(TheNeutralizer.health)
        print("3rd Attack and no death? " + "Lets change that")

    else:
        print("You have perished")


# Boss Combat set, tile x = 3, y = 4
def CombatToBoss():
    Boss.health = Boss.health - TheNeutralizer.attack
    if Boss.health > 0:
        print('Boss Health: ' + str(Boss.health))
        print("You have killed the enemy, hopefully you last until the next")
    else:
        print("The enemy has not been slain")


def CombatToPlayerB():
    TheNeutralizer.health = TheNeutralizer.health - Boss.damage
    if TheNeutralizer.health >= 0:
        print(TheNeutralizer.health)
        print("Congratulations on deafeating the boss")

    else:
        print("You have perished")


# Function for when player call for heal
def WhenHealing():
    print(TheNeutralizer.health)
    print("Healing!")
    TheNeutralizer.health = TheNeutralizer.health + HealUp.health
    print(TheNeutralizer.health)
    print("Your health has increased")
