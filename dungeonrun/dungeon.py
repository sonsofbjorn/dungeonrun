import random
from dungeonrun.monster import Monster

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
        self.monsterlist = list(self.generate_monsters(Monster.available_monster.keys()))

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

    def generate_monsters(self, foes=("giant spider", "skeleton",
                                      "orc", "troll")):
        """ This function puts monsters in all rooms if they are common enough.
        At most one of each monster in foes gets created in the room.
        """
        for row in self:
            for room in row:
                mlist = list(foes)
                while(mlist):
                    newmonster = Monster(mlist.pop(), room)
                    if (newmonster.rarity >= random.randint(0, 100)):
                        room.monsters.append(newmonster)
                        yield newmonster

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


class Treasure:
    available_items = {
                "Loose change": {"value": 2, "rarity": 40},
                "Money pouch": {"value": 6, "rarity": 20},
                "Gold jewelry": {"value": 10, "rarity": 15},
                "Gemstone": {"value": 14, "rarity": 10},
                "Small treasurechest": {"value": 20, "rarity": 5}}

    def __init__(self, item_type, room):
        self.room = room
        self.__dict__ = self.avaliable_items[item_type]
