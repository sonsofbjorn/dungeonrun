from view import View
from player import Player
from dungeon import Map
from AI import AI
import time
import random


class Controller:
    def __init__(self):
        self.view = View()

    def main_menu(self):
        self.view.print_start_menu(View.welcome_menu)

        while True:
            usr_choice = self.view.handle_input()
            # New char
            if usr_choice == "1":
                player_tuple = self.new_player()
                dungeon = self.map_size()
                startcorner = self.start_loc(dungeon)
                break
            # Load char
            elif usr_choice == "2":
                self.view.print_start_menu(View.enter_char_name)
                while True:
                    player_name = self.view.handle_input()
                    if self.player_exists(player_name):
                        player_tuple = self.load_player(player_name)
                        dungeon = self.map_size()
                        startcorner = self.start_loc(dungeon)
                        View.ai_results()
                        break
                    else:
                        self.view.print_start_menu(View.enter_char_name,
                                                   View.err_player_not_exist,
                                                   error=True)

                break
            # Use AI
            elif usr_choice == "3":
                player_tuple = self.load_AI()
                dungeon = self.map_size_AI()
                startcorner = self.start_loc_AI(dungeon)
                print(player_tuple, startcorner, dungeon)
                break
            # Highscore
            elif usr_choice == "4":
                self.view.print_start_menu(View.highscore)
                break
            # Quit
            elif usr_choice == "5":
                self.view.print_start_menu(View.good_bye)
                time.sleep(3)
                quit()
            else:
                # self.view.handle_error(View.err_choice)
                self.view.print_start_menu(View.welcome_menu,
                                           View.err_choice,
                                           error=True)
        self.start_game(*player_tuple, startcorner, dungeon)

    def map_size(self):
        self.view.print_start_menu(View.choose_size)
        while True:
            usr_choice = self.view.handle_input()
            if usr_choice == "1":
                dungeon = Map(4)
                break
            elif usr_choice == "2":
                dungeon = Map(5)
                break
            elif usr_choice == "3":
                dungeon = Map(8)
                break
            else:
                self.view.print_start_menu(View.welcome_menu,
                                           View.err_choice,
                                           error=True)
        return dungeon

    def start_loc(self, dungeon):
        self.view.print_start_menu(View.choose_corner)
        while True:
            startcorner = self.view.handle_input()
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
                self.view.print_start_menu(View.welcome_menu,
                                           View.err_choice,
                                           error=True)

        # all done
        return startcorner

    def map_size_AI(self):
        umap = 0
        map_choice = random.randrange(0, 100)
        if map_choice < 26:
            dungeon = Map(4)
        elif map_choice >= 26 & map_choice <= 74:
            dungeon = Map(5)
        elif map_choice >= 75:
            dungeon = Map(6)
        return dungeon

    def start_loc_AI(self, dungeon):
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
        return startcorner

    def start_game(self, player, role, start_room, dungeon):
        dude = Player(player, role, start_room)
        dude.current_room.isDark = False
        dude.current_room.monsters = []
        dude.current_room.treasures = []
        self.map_loop(dude, dungeon)

    def new_player(self):
        self.view.print_start_menu(View.enter_char_name)

        # character name
        while True:
            usr_choice = self.view.handle_input()

            if len(usr_choice) >= 18:
                self.view.print_start_menu(View.enter_char_name,
                                           View.err_long_name,
                                           error=True)
            elif ',' in usr_choice:
                self.view.print_start_menu(View.enter_char_name,
                                           View.err_invalid_char,
                                           error=True)
            elif self.player_exists(usr_choice):
                self.view.print_start_menu(View.enter_char_name,
                                           View.err_player_exists,
                                           error=True)
            else:
                break

        # player role
        self.view.print_start_menu(View.choose_role)
        while True:
            player_name = usr_choice
            usr_choice = self.view.handle_input()
            if usr_choice == "1":
                player_role = "knight"
                break
            elif usr_choice == "2":
                player_role = "wizard"
                break
            elif usr_choice == "3":
                player_role = "thief"
                break
            else:
                self.view.print_start_menu(View.choose_role,
                                           View.err_choice,
                                           error=True)

        # all done!
        self.save_player(player_name, player_role, 0, 0)
        return player_name, player_role

    def player_exists(self, uname):
        with open("players.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, score, highscore) = line.split(sep=",")
                if username == uname.capitalize():
                    return True, uname
        return False

    def save_player(self, uname, role, score, highscore):
        with open("players.txt", "a+") as f:
            f.write(uname.capitalize()+","+role+","+str(score)+","+str(highscore)+"\n")

    def load_player(self, uname):
        with open("players.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, score, highscore) = line.split(sep=",")
                if username == uname.capitalize():
                    return username, role
        raise Exception("Something went wrong. What? No idea... Ask Sebbe")

    def load_AI(self):
        self.view.print_start_menu(View.choose_AI)
        while True:
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
                    return username, role


    def map_loop(self, player, dungeon):
        self.view.print_game(player, self.view.draw_map2(dungeon, player), View.direction_option)
        while True:
            if player.hp < 1:
                break
            inp = self.view.handle_input()

            new_room = player.move_character(inp, dungeon)
            if new_room is False:
                print("That is not a valid direction. Try again.")
            else:
                print(player.name, "enters", player.show_location)

            if player.current_room.hasExit is True:
                print("You see a stairway, leading up towards the surface.\nDo you want to leave?")
            while len(player.current_room.monsters) > 0:
                show_monsters = "Enemies! In the room ahead, you see foes:\n"
                for monster in player.current_room.monsters:
                    show_monsters += monster.unit_type + "\n"
                print(show_monsters)
                while len(player.current_room.monsters) > 0:
                    self.combat(player)
            while len(player.current_room.treasures) > 0:
                while len(player.current_room.treasures) > 0:
                    self.loot(player)
                print("Your accumulated score is", str(player.score) + ".")

    def loot(self, char):
        for loot in char.current_room.treasures:
            char.score = int(char.score)
            char.score += loot.value
            print("oooh,", loot.item_type + "! you have added it to your backpack.\n")
            char.current_room.treasures.pop(0)


    def combat(self, char):
        initiative_list = []
        monster = char.current_room.monsters[0]
        char_init = char.roll_dice("initiative")
        monster_init = monster.roll_dice("initiative")
        if monster_init > char_init:
            initiative_list.append(monster)
            initiative_list.append(char)
        else:
            initiative_list.append(char)
            initiative_list.append(monster)
        while len(initiative_list) > 1:
            for actor in initiative_list:
                if char.hp < 1:
                    print("you have been slain by", monster.unit_type + "!")
                    initiative_list = []
                    char.current_room.monsters.clear()
                    break

                if monster.hp < 1:
                    print("you have slain the", monster.unit_type + "!")
                    initiative_list = []
                    char.current_room.monsters.pop(0)
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
                            escape = char.escape_combat()
                            if escape:
                                char.current_room = char.old_room
                                print("you have escaped")
                                initiative_list.clear()
                                break
                            else:
                                print("you have failed to escape")
                                break
                else:
                    actor.attack_function(char)
