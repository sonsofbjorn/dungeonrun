import random
from dungeon import Map
from player import Player
DEFAULT_HP = 100

class AI:
    def __init__(self, name, hero_class, start_room, score, hp):
        Player.__init__(self, name, hero_class, start_room, score, hp)

    def load_AI(self):
        while True:
            print("Please choose an AI:\n"
                  "[1] AI Knight\n"
                  "[2] AI Wizard\n"
                  "[3] AI Thief")
            uclass = input(">>")
            if uclass == "1":
                uname = "AI Knight"
                hp = 9
                break
            elif uclass == "2":
                uname = "AI Wizard"
                hp = 4
                break
            elif uclass == "3":
                uname = "AI Thief"
                hp = 5
                break
            else:
                print("Incorrect input")
        with open("AI.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, score, highscore) = line.split(sep=",")
                if username == uname:
                    print("Loaded " + username
                          + "\nAI current score is " + str(score)
                          + "\nAI highest score is " + str(highscore))
                    return username, role, role, score, hp

    def select_mapsize(self):
        umap = 0
        map_choice = random.randrange(0, 100)
        if map_choice < 26:
            umap = 4
        elif map_choice >= 26 & map_choice <= 74:
            umap = 5
        elif map_choice >= 75:
            umap = 6
        print("AI chose mapsize", umap)
        return umap

    def start_location(self, dungeon):
        corner_choice = random.randrange(0, 4)
        if corner_choice == 1:
            startcorner = dungeon.corner["NW"]
            dungeon.get_room(dungeon.size-1, dungeon.size-1).hasExit = True
        elif corner_choice == 2:
            startcorner = dungeon.corner["NE"]
            dungeon.get_room(0, dungeon.size-1).hasExit = True
        elif corner_choice == 2:
            startcorner = dungeon.corner["SW"]
            dungeon.get_room(dungeon.size-1, 0).hasExit = True
        else:
            startcorner = dungeon.corner["SE"]
            dungeon.get_room(0, 0).hasExit = True
        print("AI chose corner", startcorner.position)
        return startcorner

    def print_start_location(self):
        print("I am in", self.start_corner.position)


temp = AI.load_AI(0)

AI_Player = AI(*temp)

dungeon = Map(AI_Player.select_mapsize())

AI_Player.start_corner = AI_Player.start_location(dungeon)

AI_Player.print_start_location()

print(isinstance(AI_Player, Player))

player_tester = Player("dude", "knight", AI_Player.start_corner)

print(isinstance(player_tester, Player))

print(issubclass(Player, AI))
print(issubclass(AI, Player))
'''
temp = load_player(uname)
    return username, role, score
dungeon = create_dungeon(select_mapsize())
startlc = start_location(dungeon)
start_game(*temp, startlc, dungeon)


'''
