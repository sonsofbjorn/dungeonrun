from dungeonrun import player
from dungeonrun import dungeon


def create_dungeon(size):
    instance = dungeon.Map(size)
    return instance


def start_location(dungeon):
    while True:
        print("Choose your starting location:\n"
              "[1] North-West\n"
              "[2] North-East\n"
              "[3] South-West\n"
              "[4] South-East\n")
        startcorner = input(">>")
        if startcorner == "1":
            startcorner = dungeon.corner["NW"]
            dungeon.get_room(dungeon.size-1, dungeon.size-1).hasExit = True
            break
        elif startcorner == "2":
            startcorner = dungeon.corner["NE"]
            dungeon.get_room(0, dungeon.size-1).hasExit = True
            break
        elif startcorner == "3":
            startcorner = dungeon.corner["SW"]
            dungeon.get_room(dungeon.size-1, 0).hasExit = True
            break
        elif startcorner == "4":
            startcorner = dungeon.corner["SE"]
            dungeon.get_room(0, 0).hasExit = True
            break
        else:
            print("Incorrect input!")
    return startcorner


def select_mapsize():
    while True:
        print("Please choose your mapsize:\n"
              "[1] 4x4\n"
              "[2] 5x5\n"
              "[3] 8x8")
        umap = input(">>")
        if umap == "1":
            umap = 4
            break
        elif umap == "2":
            umap = 5
            break
        elif umap == "3":
            umap = 8
            break
        else:
            print("Incorrect input")
    return umap


def choose_role():
    while True:
        print("Please choose your role:\n"
              "[1] Knight\n"
              "[2] Wizard\n"
              "[3] Thief")
        uclass = input(">>")
        if uclass == "1":
            uclass = "knight"
            break
        elif uclass == "2":
            uclass = "wizard"
            break
        elif uclass == "3":
            uclass = "thief"
            break
        else:
            print("Incorrect input")
    return uclass


def save_new_player(uname, role, score, highscore):
    with open("players.txt", "a+") as f:
        f.write(uname.capitalize()+","+role+","+str(score)+","+str(highscore)+"\n")


def player_exists(uname):
    with open("players.txt", "r") as f:
        file = f.readlines()
        for line in file:
            (username, role, score, highscore) = line.split(sep=",")
            if username == uname.capitalize():
                return True
    return False


def load_player(uname):
    with open("players.txt", "r") as f:
        file = f.readlines()
        for line in file:
            (username, role, score, highscore) = line.split(sep=",")
            if username == uname.capitalize():
                print("Welcome back "+username
                      +"\nYour current role is a "+role
                      +"\nYour highest score is "+str(score)
                      +"\nOverall highest score is "+str(highscore))
                return username, role, score
    raise Exception("Something went wrong. What? No idea... Ask Sebbe")


def start_game(username, role, score, start_room, dungeon):

    dude = player.Player(username, role, start_room, score)
    dude.current_room.dark = False
    # monster + treasure generation
    map_loop(dude, dungeon)


def map_loop(char, dungeon):
    while True:
        print(char.name + ", you are in", char.show_location)
        print(char.name + ", where do you want to go? West, North, East, or South?") # This should be neatly handled
        # in the viewer eventually (dynamically displaying depending on doors present)
        inp = input(">>")
        new_room = dungeon.enter_door(char.current_room, inp)
        if new_room is False:
            print("That is not a valid direction. Try again.")
        else:
            char.move_character(new_room)
            print(char.name , "enters", char.show_location)

        if char.current_room.hasExit is True:
            print("You see a stairway, leading up towards the surface.\nDo you want to leave?")
        elif len(char.current_room.monsters) < 0:
            print("Hello monsters")
        elif len(char.current_room.treasures) < 0:
            print("here be treasures")


class Menu:

    def main_menu(self):
        while True:
            print("Welcome to... DUNGEON RUN!\n"
                  "[1] New Character\n"
                  "[2] Load Character\n"
                  "[3] Highscore\n"
                  "[4] Quit")

            menuchoice = input(">>")
            if menuchoice == "1":
                while True:
                    print("Please create Username")
                    uname = input(">>")
                    if not player_exists(uname.capitalize()):
                        uclass = choose_role()
                        dungeon = create_dungeon(select_mapsize())
                        startlc = start_location(dungeon)
                        save_new_player(uname, uclass, 0, 0)
                        start_game(*load_player(uname), startlc, dungeon)
                        break
                    else:
                        print("Username already exists!")
                # skicka vidare till en funktion

            elif menuchoice == "2":
                print("Please enter Username")
                uname = input(">>")
                if player_exists(uname):
                    temp = load_player(uname)
                    dungeon = create_dungeon(select_mapsize())
                    startlc = start_location(dungeon)
                    start_game(*temp, startlc, dungeon)
                else:
                    print("Username does not exits, Please create a new username")

            elif menuchoice == "3":
                print("Highscore")
                print("Press [ENTER] to continue")
                input(">>")

            elif menuchoice == "4":
                print("See you next time!")
                break
            else:
                print("Incorrect input!")


