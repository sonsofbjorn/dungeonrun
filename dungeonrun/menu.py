from player import Player
from dungeon import Map


class Menu:
    def main_menu(self):
        while True:
            print("Welcome to... DUNGEON RUN!\n"
                  "[1] New Character\n"
                  "[2] Load Character\n"
                  "[3] Remove Character\n"
                  "[4] Highest score\n"
                  "[5] Quit")

            menuchoice = input(">>")
            if menuchoice == "1":
                while True:
                    print("Please create a 'Name' for the role")
                    uname = input(">>")
                    if not player_exists(uname.capitalize()):
                        uclass = choose_role()
                        dungeon = create_dungeon(select_mapsize())
                        startlc = start_location(dungeon)
                        save_player(uname, uclass, 0, 0)
                        start_game(*load_player(uname), startlc, dungeon)
                        break
                    else:
                        print("Name already exists!")
                # skicka vidare till en funktion

            elif menuchoice == "2":
                print("Please enter the Name")
                uname = input(">>")
                if player_exists(uname):
                    temp = load_player(uname)
                    dungeon = create_dungeon(select_mapsize())
                    startlc = start_location(dungeon)
                    start_game(*temp, startlc, dungeon)
                else:
                    print("Name does not exits, Please create a 'Name' for the role.")

            elif menuchoice == "3":
                print("Please enter Name")
                uname = input(">>")
                if player_exists(uname):
                    delete_player(uname)
                    print(uname.capitalize() + " is deleted!")
                else:
                    print("Name does not exist!")

            elif menuchoice == "4":
                print("Highest score")
                print("Press [ENTER] to continue")
                input(">>")

            elif menuchoice == "5":
                print("See you next time!")
                break
            else:
                print("Incorrect input!")


def create_dungeon(size):
    instance = Map(size)
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


def save_player(uname, role, score, highscore):
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
                      + "\nYour current character is a", role
                      + "\nYour highest score is " + str(score)
                      + "\nOverall highest score is " + str(highscore))
                return username, role, score
    raise Exception("Something went wrong. What? No idea... Ask Sebbe")


def delete_player(uname):
    with open("players.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if str(uname.capitalize()) not in line:
                f.write(line)
        f.truncate()
        return


def start_game(username, role, score, start_room, dungeon):
    dude = Player(username, role, start_room, score)
    dude.current_room.dark = False
    dude.current_room.monsters = []
    dude.current_room.treasures = []
    map_loop(dude, dungeon)


def map_loop(char, dungeon):
    while True:
        if char.hp < 1:
            break
        print(char.name + ", you are in", char.show_location)
        print(char.name + ", where do you want to go? West, North, East, or South?")
        inp = input(">>")
        # This should be neatly handled in the viewer eventually (dynamically displaying depending on doors present)

        new_room = char.move_character(inp, dungeon)
        if new_room is False:
            print("That is not a valid direction. Try again.")
        else:
            print(char.name, "enters", char.show_location)

        if char.current_room.hasExit is True:
            print("You see a stairway, leading up towards the surface.\nDo you want to leave?")
        while len(char.current_room.monsters) > 0:
            show_monsters = "Enemies! In the room ahead, you see foes:\n"
            for monster in char.current_room.monsters:
                show_monsters += monster.unit_type + "\n"
            print(show_monsters)
            while len(char.current_room.monsters) > 0:
                combat(char)
        while len(char.current_room.treasures) > 0:
            while len(char.current_room.treasures) > 0:
                loot(char)
            print("Your accumulated score is", str(char.score) + ".")


def loot(char):
    for loot in char.current_room.treasures:
        char.score = int(char.score)
        char.score += loot.value
        print("Oooh,", loot.item_type + "! you have added it to your backpack.\n")
        char.current_room.treasures.pop(0)


def combat(player):
    initiative_list = []
    monster = player.current_room.monsters[0]
    char_init = player.roll_dice("initiative")
    monster_init = monster.roll_dice("initiative")
    if monster_init > char_init:
        initiative_list.append(monster)
        initiative_list.append(player)
    else:
        initiative_list.append(player)
        initiative_list.append(monster)
    while len(initiative_list) > 1:
        for actor in initiative_list:
            if player.hp < 1:
                print("you have been slain by", monster.unit_type + "!")
                initiative_list = []
                player.current_room.monsters.clear()
                game_over()
                # quit game
                break

            if monster.hp < 1:
                print("you have slain the", monster.unit_type + "!")
                initiative_list = []
                player.current_room.monsters.pop(0)
                break
            elif isinstance(actor, Player):
                while True:
                    print("choose your action:\n"
                          "[1] attack\n"
                          "[2] flee")
                    choice = input(">>")
                    if choice == "1":
                        actor.attack_function(monster)
                        break
                    elif choice == "2":
                        escape = player.escape_combat()
                        if escape:
                            player.current_room = player.old_room
                            print("you have escaped")
                            initiative_list.clear()
                            break
                        else:
                            print("you have failed to escape")
                            break
            else:
                actor.attack_function(player)


def game_over():
    print("Game over.")

Menu.main_menu(0)
