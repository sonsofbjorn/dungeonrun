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
        """ Makes a dungeon of room objects and fills it with
        doors, monsters and treasures """
        if size not in [4, 5, 8]:
            raise Exception("Wrong size")
        self.size = size
        self.matrix = tuple(tuple(Room(x, y)
                            for x in range(size))
                            for y in range(size))
        self.generate_doors()

        # monsterlist is a list of generated monster objects in the dungeon
        # Monsters know where they are (they have a room object as position)
        # same goes for treasures
        self.monsterlist = list(self.fill_room(Monster.available))
        self.treasurelist = list(self.fill_room(Treasure.available))

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

    def fill_room(self, things):
        """
        Takes a list of things (treasures or monsters)
        This function puts things in all rooms if they are common enough.
        At most one of each thing in things gets created in the room.
        """
        for row in self:
            for room in row:
                for thing in things:
                    if thing in Monster.available:
                        thing = Monster(thing, room)
                    elif thing in Treasure.available:
                        thing = Treasure(thing, room)
                    else: raise Exception("Can't put unknown items in room.")
                    if thing.rarity >= random.randint(0,100):
                        if isinstance(thing, Monster):
                            room.monsters.append(thing)
                        else: room.treasures.append(thing)
                        yield thing

    def print_monsters(self):
        """ This is a debug function """
        for monster in self.monsterlist:
            print(monster.room.position, monster.unit_type.uni)
        return ("Map contains {1} monsters in {0} rooms"
                .format(self.size**2, len(self.monsterlist)))


class Room:
    def __init__(self, x, y, is_dark=True, has_exit=False,
                 monsters=[], treasures=[]):
        self.is_dark, self.has_exit = is_dark, has_exit
        self.monsters = []  # Why doesn't the kwarg above suffice?
        self.treasures = []

        # DOORS N E S W
        self.doors = {"N": True, "E": True, "S": True, "W": True}

        # self.doors = [True, True, True, True]

        # Position X,Y tuple
        self.position = (x, y)

    def get_room_monsters(self):
        """
        Returns a list of monster types.
        Each elemement is a string!
        """
        room_monsters = list()
        for monster in self.monsters:
            room_monsters.append(monster.unit_type)
        return room_monsters


class Monster:

    available = ("giant spider", "skeleton", "orc", "troll")

    def __init__(self, unit_type, room):

        self.unit_type = unit_type
        self.room = room

        if self.unit_type == "giant spider":
            self.initiative = 7
            self.hp = 1
            self.attack = 2
            self.dexterity = 3
            self.rarity = 20
        if self.unit_type == "skeleton":
            self.initiative = 4
            self.hp = 2
            self.attack = 3
            self.dexterity = 3
            self.rarity = 15
        if self.unit_type == "orc":
            self.initiative = 6
            self.hp = 3
            self.attack = 4
            self.dexterity = 4
            self.rarity = 10
        if self.unit_type == "troll":
            self.initiative = 2
            self.hp = 4
            self.attack = 7
            self.dexterity = 2
            self.rarity = 5

        self.max_hp = self.hp


class Treasure:
    available = ("loose change","money pouch",
    "gold jewelry","gemstone","small treasurechest")

    def __init__(self, item_type, room):
        self.item_type = item_type
        self.room = room

        if self.item_type  == "loose change":
            self.value = 2
            self.rarity = 40
        elif self.item_type  == "money pouch":
            self.value = 6
            self.rarity = 20
        elif self.item_type  == "gold jewelry":
            self.value = 10
            self.rarity = 15
        elif self.item_type  == "gemstone":
            self.value = 14
            self.rarity = 10
        elif self.item_type  == "small treasurechest":
            self.value = 20
            self.rarity = 5
