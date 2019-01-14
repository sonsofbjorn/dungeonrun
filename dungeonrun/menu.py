from dungeonrun import player
from dungeonrun import dungeon


def createDungeon(size):
    instance = dungeon.Map(size)
    return instance


def startlocation(dungeon):
    while True:
        print("Choose your starting location:\n"
              "[1] North-West\n"
              "[2] North-East\n"
              "[3] South-West\n"
              "[4] South-East\n")
        startcorner = input(">>")
        if startcorner == "1":
            startcorner = dungeon.get_room(0, 0)
            dungeon.get_room(dungeon.size-1, dungeon.size-1).hasExit = True
            break
        elif startcorner == "2":
            startcorner = dungeon.get_room(dungeon.size-1, 0)
            dungeon.get_room(dungeon.size-1, 0).hasExit = True
            break
        elif startcorner == "3":
            startcorner = dungeon.get_room(0, dungeon.size-1)
            dungeon.get_room(0, dungeon.size-1).hasExit = True
            break
        elif startcorner == "4":
            startcorner = dungeon.get_room(dungeon.size-1, dungeon.size-1)
            dungeon.get_room(0, 0).hasExit = True
            break
        else:
            print("Incorrect input!")
    return startcorner


def selectmapsize():
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


def chooserole():
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


def saveNewPlayer(uname, role, score, highscore):
    with open("players.txt", "a+") as f:
        f.write(uname.capitalize()+","+role+","+str(score)+","+str(highscore)+"\n")


def playerExists(uname):
    with open("players.txt", "r") as f:
        file = f.readlines()
        for line in file:
            (username, role, score, highscore) = line.split(sep=",")
            if username == uname.capitalize():
                return True
    return False


def loadPlayer(uname):
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


def startGame(username, role, score, start_room, dungeon):

    dude = player.Player(username, role, start_room, score)
    dude.current_room.dark = False
    # monster + treasure generation
    mapLoop(dude, dungeon)


def mapLoop(char, dungeon):

    while True:
        print(char.name + ", you are in", char.show_location)
        print(char.name + ", where do you want to go? West, North, East, or South?")
        inp = input(">>")
        new_room = dungeon.enter_door(char.current_room, inp)
        if new_room is not False:
            char.move_character(new_room)
            print(char.show_location)
            break





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
                    if not playerExists(uname.capitalize()):
                        uclass = chooserole()
                        dungeon = createDungeon(selectmapsize())
                        startlc = startlocation(dungeon)
                        saveNewPlayer(uname, uclass, 0, 0)
                        startGame(*loadPlayer(uname), startlc, dungeon)
                        break
                    else:
                        print("Username already exists!")
                # skicka vidare till en funktion

            elif menuchoice == "2":
                print("Please enter Username")
                uname = input(">>")
                if playerExists(uname):
                    temp = loadPlayer(uname)
                    dungeon = createDungeon(selectmapsize())
                    startlc = startlocation(dungeon)
                    startGame(*temp, startlc, dungeon)
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


