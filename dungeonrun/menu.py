from dungeonrun import player


def startlocation():
    while True:
        print("Choose your starting location:\n"
              "[1] North-West\n"
              "[2] North-East\n"
              "[3] South-West\n"
              "[4] South-East\n")
        inp = input(">>")
        if inp == "1":
            inp = "nw"
            break
        elif inp == "2":
            inp = "ne"
            break
        elif inp == "3":
            inp = "sw"
            break
        elif inp == "4":
            inp = "se"
            break
        else:
            print("Incorrect input!")
    return inp


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
        f.write(uname+","+role+","+str(score)+","+str(highscore)+"\n")


def playerExists(uname):
    with open("players.txt", "r") as f:
        file = f.readlines()
        for line in file:
            (username, role, score, highscore) = line.split(sep=",")
            if username == uname:
                return True
    return False


class Menu:
    while True:
        print("Välkommen till dungeonrun!\n"
              "[1] New Character\n"
              "[2] Load Character\n"
              "[3] Quit")

        menuchoice = input(">>")
        if menuchoice == "1":
            print("Please enter you Username")
            uname = input(">>")
            if not playerExists(uname):
                uclass = chooserole()
                mapsize = selectmapsize()
                startlc = startlocation()
                saveNewPlayer(uname, uclass, 0, 0)
                user = player.Player(uname, uclass.lower(), startlc)
            else:
                print("asdahssshshshs")
            # skicka vidare till en funktion

        elif menuchoice == "2":
            print("")


