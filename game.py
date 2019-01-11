class Map:
    def __init__(self, size):
        if size not in [4,5,8]: raise Exception("Wrong size")
        self.size = size
        self.room = tuple(tuple(Room() for col in range(size)) for row in range(size)
        corner = { 
            'NW': self.room[0][0],
            'NE': self.room[0][size-1],
            'SW': self.room[size-1][0], 
            'SE': self.room[size-1][size-1] 
            }


class Room:

    def __init__(self, isDark=True, hasExit=False,
            monsters=[], treasures=[], doors=[]):
        self.dark, self.hasExit = isDark, hasExit
        self.monsters, self.treasures = monsters, treasures
        self.doors = doors

