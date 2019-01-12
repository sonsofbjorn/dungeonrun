'''
X = COL
Y = ROW

MAP EXAMPLE: SMALL 4x4
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

        corner = {
            'NW': self.matrix[0][0],
            'NE': self.matrix[0][size-1],
            'SW': self.matrix[size-1][0],
            'SE': self.matrix[size-1][size-1]
            }

        # North ->
        for x in range(size):
            room = self.room(x, 0)
            room.doors["N"] = False

        # Down East
        for y in range(size):
            room = self.room(size-1, y)
            room.doors["E"] = False

        # South ->
        for x in range(size):
            room = self.room(x, size-1)
            room.doors["S"] = False

        for y in range(size):
            room = self.room(0, y)
            room.doors["W"] = False

    # This is here becose in matrix row is first instead of col
    def room(self, x, y):
        return self.matrix[y][x]

    def enter_door(self, current_room, door):
        new_room = current_room
        x = current_room.position[0]
        y = current_room.position[1]
        if door.lower() == "west":
            new_room = self.room(x-1, y)
        elif door.lower() == "north":
            new_room = self.room(x, y-1)
        elif door.lower() == "east":
            new_room = self.room(x+1, y)
        elif door.lower() == "south":
            new_room = self.room(x, y+1)
        else:
            raise Exception("How did you enter else?")
        return new_room


class Room:

    def __init__(self, x, y, isDark=True, hasExit=False,
                 monsters=[], treasures=[]):
        self.dark, self.hasExit = isDark, hasExit
        self.monsters, self.treasures = monsters, treasures

        # DOORS N E S W
        self.doors = {"N": True, "E": True, "S": True, "W": True}

        #self.doors = [True, True, True, True]

        # Position X,Y tuple
        self.position = (x, y)

    def getCoords(self):
        print(self.position)


