import random

'''
X = COL
Y = ROW

MAP EXAMPLE: SMALL 4x4
(0, 0)(1, 0)(2, 0)(3, 0)
(0, 1)(1, 1)(2, 1)(3, 1)
(0, 2)(1, 2)(2, 2)(3, 2)
(0, 3)(1, 3)(2, 3)(3, 3)
'''


class Map:
    def __init__(self, size):
        if size not in [4, 5, 8]:
            raise Exception("Wrong size")
        self.size = size
        self.matrix = tuple(tuple(Room(x, y)
                            for x in range(size))
                            for y in range(size))
        self.generate_doors()
        # monsterlist is a list of generated monster objects in the dungeon
        # Monsters know where they are (they have a room object as position)
        self.monsterlist = list(self.generate_monsters(
            Monster.available_monsters))

        self.treasurelist = list(self.generate_treasure(
            Treasure.available_items.keys()))

        self.corner = {
            'NW': self.get_room(0, 0),
            'NE': self.get_room(size-1, 0),
            'SW': self.get_room(0, size-1),
            'SE': self.get_room(size-1, size-1)
            }

    def __iter__(self):
        for rooms in self.matrix:
            yield rooms

    def generate_doors(self):
        """This generate the doors for the rooms"""
        # NW -> NE
        for x in range(self.size):
            room = self.get_room(x, 0)
            room.doors["N"] = False

        # NE -> SE
        for y in range(self.size):
            room = self.get_room(self.size-1, y)
            room.doors["E"] = False

        # SE -> SW
        for x in range(self.size):
            room = self.get_room(x, self.size-1)
            room.doors["S"] = False

        # SW -> NE
        for y in range(self.size):
            room = self.get_room(0, y)
            room.doors["W"] = False

    # This is here because in matrix row is first instead of col
    def get_room(self, x, y):
        return self.matrix[y][x]

    def generate_monsters(self, foes):
        """ This function puts monsters in all rooms if they are common enough.
        At most one of each monster in foes gets created in the room.
        """
        for row in self:
            for room in row:
                mlist = list(foes)
                while mlist:
                    newmonster = Monster(mlist.pop(), room)
                    if newmonster.rarity >= random.randint(0, 100):
                        room.monsters.append(newmonster)
                        yield newmonster

    def generate_treasure(self, gold=("Loose change", "Money pouch",
                                      "Gold jewelry", "Gemstone", "Small treasure chest")):
        """ CASH CASH BABY
        """
        for row in self:
            for room in row:
                tlist = list(gold)
                while(tlist):
                    newtreasure = Treasure(tlist.pop(), room)
                    if newtreasure.rarity >= random.randint(0, 100):
                        room.treasures.append(newtreasure)
                        yield newtreasure

    def print_monsters(self):
        """ This is a debug function """
        for monster in self.monsterlist:
            print(monster.room.position, monster.unit_type.uni)
        return ("Map contains {1} monsters in {0} rooms"
                .format(self.size**2, len(self.monsterlist)))


class Room:
    def __init__(self, x, y, isDark=True, hasExit=False,
                 monsters=[], treasures=[]):
        self.dark, self.hasExit = isDark, hasExit
        self.monsters = []  # Why doesn't the kwarg above suffice?
        self.treasures = []

        # DOORS N E S W
        self.doors = {"N": True, "E": True, "S": True, "W": True}

        # self.doors = [True, True, True, True]

        # Position X,Y tuple
        self.position = (x, y)


class Monster:

    available_monsters = ("giant spider", "skeleton", "orc", "troll")

    def __init__(self, unit_type, room):

        self.unit_type = unit_type
        self.room = room

        if self.unit_type.lower() == "giant spider":
            self.initiative = 7
            self.hp = 1
            self.attack = 2
            self.dexterity = 3
            self.rarity = 20

        if self.unit_type.lower() == "skeleton":
            self.initiative = 4
            self.hp = 2
            self.attack = 3
            self.dexterity = 3
            self.rarity = 15

        if self.unit_type.lower() == "orc":
            self.initiative = 6
            self.hp = 3
            self.attack = 4
            self.dexterity = 4
            self.rarity = 10

        if self.unit_type.lower() == "troll":
            self.initiative = 2
            self.hp = 4
            self.attack = 7
            self.dexterity = 2
            self.rarity = 5

    def roll_dice(self, dice_type):
        if dice_type == "attack":
            dice_type = self.attack
        elif dice_type == "dexterity":
            dice_type = self.dexterity
        elif dice_type == "initiative":
            dice_type = self.initiative
        value = 0
        for x in range(0, dice_type):
            value += random.randrange(0, dice_type)
        return value

    def attack_function(self, player):
        attacker_roll = self.roll_dice("attack")
        player_roll = player.roll_dice("dexterity")
        if attacker_roll > player_roll:
            if player.hero_class == "knight":
                # Another IF needed to see if player blocks attack
                print("something something knight shield")
            print(player.name, "is hit by the", str(self.unit_type) + "!")
            player.hp -= 1
            print("You have", player.hp, "hp remaining!")
        else:
            print("The", self.unit_type, "attacks", player.name + ", but misses!")


class Treasure:
    available_items = {}

    def __init__(self, item_type, room):
        self.item_type = item_type
        self.room = room

        if self.item_type.lower() == "loose change":
            self.value = 2
            self.rarity = 40
        elif self.item_type.lower() == "money pouch":
            self.value = 6
            self.rarity = 20
        elif self.item_type.lower() == "gold jewelry":
            self.value = 10
            self.rarity = 15
        elif self.item_type.lower() == "gemstone":
            self.value = 14
            self.rarity = 10
        elif self.item_type.lower() == "small treasurechest":
            self.value = 20
            self.rarity = 5
