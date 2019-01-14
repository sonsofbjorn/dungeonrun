from dungeonrun import dungeon
from dungeonrun import player

class View:

    def __init__(self):
        m = dungeon.Map(4)

        p = player.Player("bob", "knight", dungeon.Room(0, 1))

        for row in m:
            for room in row:
                if p == room.position:
                    print("1", end=" ")
            print()
