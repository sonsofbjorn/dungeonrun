from dungeonrun import dungeon
from dungeonrun import player
from dungeonrun import monster
from dungeonrun import menu

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

    def draw_start_location_options(self):
        startcorner = input(">>")
        print("Choose your starting location:\n"
                "[1] North-West\n"
                "[2] North-East\n"
                "[3] South-West\n"
                "[4] South-East\n")
        return startcorner

    def draw_map_loop(self):
        print(self.p.name + ", you are in", self.p.show_location)
        print(self.p.name + ", where do you want to go? West, North, East, or South?")
        inp = input(">>")
        return inp
