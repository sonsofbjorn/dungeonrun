from dungeonrun import dungeon
from dungeonrun import player

class View:

    def __init__(self, dungeon, player):
        self.m = dungeon
        self.p = player

    def draw_map(self):
        for row in self.m:
            for room in row:
                if room.position == self.p.show_location:
                    print("o", end="")

                elif room.dark:
                    print("▓", end="")
                else:
                    print("░", end="")
            print()
