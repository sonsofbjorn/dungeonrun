class Map:
    def __init__(self, size):
        if size not in [4, 5, 8]: raise Exception("Wrong size")
        self.size = size
        self.matrix = tuple(tuple(Room(col, row) for row in range(size)) for col in range(size))

        corner = {
                'NW': self.matrix[0][0],
                'NE': self.matrix[0][size-1],
                'SW': self.matrix[size-1][0],
                'SE': self.matrix[size-1][size-1]
                }

    def generateRooms(self):
        for room in self.matrix[3]:
            room.doors[0] = False
class Room:

    def __init__(self, col, row, isDark=True, hasExit=False,
                 monsters=[], treasures=[], doors=[True, True, True, True]):
        self.dark, self.hasExit = isDark, hasExit
        self.monsters, self.treasures = monsters, treasures

        # DOORS N E S W
        self.doors = doors

        # Position X,Y tuple
        self.position = (col, row)

