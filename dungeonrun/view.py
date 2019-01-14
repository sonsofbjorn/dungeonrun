from dungeonrun import dungeon
from dungeonrun import player

class View:

    def __init__(self, dungeon, player):
        self.m = dungeon
        self.p = player

    def draw_map(self):
        for row in self.m:
            for x in range(3):
                for room in row:
                    if room.position == self.p.show_location:
                        if x == 1:
                            print(" ", end="")
                            print(" ╳  ", end="")
                            print(" ", end="")
                        else:
                            print("   ", end="")
                            print("", end="")
                            print("   ", end="")
                    elif room.hasExit and room.dark is False:
                        if x == 1:
                            print("░", end="")
                            print("exit", end="")
                            print("░", end="")
                        else:
                            print("░░░", end="")
                            print("", end="")
                            print("░░░", end="")


                    elif room.dark:
                        print("▓▓", end="")
                        print("▓▓", end="")
                        print("▓▓", end="")
                    else:
                        print("░░", end="")
                        print("░░", end="")
                        print("░░", end="")
                print()
