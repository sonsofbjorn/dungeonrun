from view import View
from player import Player
from dungeon import Map
import time
import random


class Controller:
    def __init__(self):
        self.view = View()

    def main_menu(self):
        """
        Logic for main menu. Here we get information from the user.
        player_tuple is a tuple, containing name and role
        start_loc_menu is a string containing, "NW" and so on.
        dungeon_size is an int.

        When we have all the necessary information we run init_objects.
        That function will generate the objects and then pass on into the
        game_loop.
        Returns AI = True if player chose an AI.
        """
        # PRINTS MAIN MENU
        self.view.print_main_menu(View.welcome_menu)

        # 1. NEW PLAYER, 2. LOAD CHAR, 3. HIGHSCORE, 4.
        while True:
            usr_choice = self.view.handle_input()

            if usr_choice == "1":
                player_tuple = self.new_player_menu()
                dungeon_size = self.map_size_menu()
                start_loc = self.start_loc_menu()
                break

            elif usr_choice == "2":
                self.view.print_main_menu(View.enter_char_name)
                while True:
                    player_name = self.view.handle_input()
                    if self.player_exists(player_name):
                        player_tuple = self.load_player(player_name)
                        dungeon_size = self.map_size_menu()
                        start_loc = self.start_loc_menu()
                        break
                    else:
                        self.view.print_main_menu(View.enter_char_name,
                                                  View.err_player_not_exist,
                                                  error=True)
                        break
            # Use AI
            elif usr_choice == "3":
                player_tuple = self.load_AI()
                dungeon_size = self.map_size_AI()
                start_loc = self.start_loc_AI()
                break
            # Highscore
            elif usr_choice == "4":
                self.view.print_main_menu(View.highscore)
                break
            # Quit
            elif usr_choice == "5":
                self.view.print_main_menu(View.good_bye)
                time.sleep(3)
                quit()
            else:
                self.view.print_main_menu(View.welcome_menu,
                                          View.err_choice,
                                          error=True)
        if usr_choice == "3":
            self.init_objects(*player_tuple, start_loc, dungeon_size, True)
        else:
            self.init_objects(*player_tuple, start_loc, dungeon_size)

    def map_size_menu(self):
        """
        Menu for asking what size the player wants to play on.
        Returns an int to be used in init_objects
        """
        self.view.print_main_menu(View.choose_size)
        while True:
            usr_choice = self.view.handle_input()
            if usr_choice == "1":
                dungeon_size = 4
                break
            elif usr_choice == "2":
                dungeon_size = 5
                break
            elif usr_choice == "3":
                dungeon_size = 8
                break
            else:
                self.view.print_main_menu(View.welcome_menu,
                                          View.err_choice,
                                          error=True)
        return dungeon_size

    def start_loc_menu(self):
        """
        Asks viwer to show menu for starting location
        returns the choice as a string
        """
        self.view.print_main_menu(View.choose_corner)
        while True:
            usr_choice = self.view.handle_input()
            if usr_choice == "1":
                start_loc = "NW"
                break
            elif usr_choice == "2":
                start_loc = "NE"
                break
            elif usr_choice == "3":
                start_loc = "SW"
                break
            elif usr_choice == "4":
                start_loc = "SE"
                break
            else:
                self.view.print_main_menu(View.welcome_menu,
                                          View.err_choice,
                                          error=True)
        # This string is sent into init_objects function later
        return start_loc

    def map_size_AI(self):
        map_size = 0
        map_choice = random.randrange(0, 100)
        if map_choice < 26:
            map_size = 5
        elif map_choice >= 26 & map_choice <= 74:
            map_size = 5
        elif map_choice >= 75:
            map_size = 6
        return map_size

    def start_loc_AI(self):
        corner_choice = random.randrange(0, 4)
        if corner_choice == 1:
            start_loc = "NW"
        elif corner_choice == 2:
            start_loc = "NE"
        elif corner_choice == 2:
            start_loc = "SW"
        else:
            start_loc = "SE"
        return start_loc

    def new_player_menu(self):
        """
        Here we get all the necessary information to create a player object
        later in init_objects.
        Returns a tuple with name and role
        """
        self.view.print_main_menu(View.enter_char_name)

        # character name
        while True:
            usr_choice = self.view.handle_input()

            if len(usr_choice) >= 18:
                self.view.print_main_menu(View.enter_char_name,
                                          View.err_long_name,
                                          error=True)
            elif ',' in usr_choice:
                self.view.print_main_menu(View.enter_char_name,
                                          View.err_invalid_char,
                                          error=True)
            elif self.player_exists(usr_choice):
                self.view.print_main_menu(View.enter_char_name,
                                          View.err_player_exists,
                                          error=True)
            else:
                break

        # player role
        self.view.print_main_menu(View.choose_role)
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
                self.view.print_main_menu(View.choose_role,
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
            f.write(uname.capitalize()
                    + ","+role+","+str(score)+","+str(highscore)+"\n")

    def load_player(self, uname):
        """
        This loads a player from players.txt
        Returns a tuple with name and role which will be used in init_objects
        """
        with open("players.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, score, highscore) = line.split(sep=",")
                if username == uname.capitalize():
                    return username, role
        raise Exception("Something went wrong. What? No idea... Ask Sebbe")

    def load_AI(self):
        '''
        Loads a knight, wiz or thief character from AI.txt
        Returns a tuple with name and role
        '''
        self.view.print_main_menu(View.choose_AI)
        while True:
            uclass = input(">>")
            if uclass == "1":
                uname = "AI Knight"
                break
            elif uclass == "2":
                uname = "AI Wizard"
                break
            elif uclass == "3":
                uname = "AI Thief"
                break
            else:
                print("Incorrect input")
        with open("AI.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, score, highscore) = line.split(sep=",")
                if username == uname:
                    return username, role

    def init_objects(self, player, role, start_loc, dungeon_size, ai_check=False):
        """
        this function will init objects
        player, role, start_loc is a string.
        dungeon_size is an int,
        ai_check is a boolean (default False) to see if player is an AI
        This function will generate game objects,
        dungeon, start_room and player
        """
        # Create dungeon
        dungeon = Map(dungeon_size)

        # Get start room and set exit
        if start_loc == "NW":
            start_room = dungeon.corner["NW"]
            dungeon.get_room(dungeon.size-1, dungeon.size-1).hasExit = True
        elif start_loc == "NE":
            start_room = dungeon.corner["NE"]
            dungeon.get_room(0, dungeon.size-1).hasExit = True
        elif start_loc == "SW":
            start_room = dungeon.corner["SW"]
            dungeon.get_room(dungeon.size-1, 0).hasExit = True
        elif start_loc == "SE":
            start_room = dungeon.corner["SE"]
            dungeon.get_room(0, 0).hasExit = True

        player = Player(player, role, start_room)
        if ai_check is True:
            player.AI = True
            player.start_room = start_room
            self.ai_find_exit(player, dungeon)
        player.current_room.isDark = False
        player.current_room.monsters = []
        player.current_room.treasures = []
        self.game_loop(player, dungeon)  # Should we run this here?

    def ai_find_exit(self, player, dungeon):
        if player.current_room.position == (0, 0):
            player.destination = dungeon.get_room(dungeon.size-1, dungeon.size-1)
        elif player.current_room.position == (dungeon.size-1, 0):
            player.destination = dungeon.get_room(0, dungeon.size-1)
        elif player.current_room.position == (0, dungeon.size-1):
            player.destination = dungeon.get_room(dungeon.size-1, 0)
        elif player.current_room.position == (dungeon.size-1, dungeon.size-1):
            player.destination = dungeon.get_room(0, 0)

    def game_loop(self, player, dungeon):
        """
        Main game loop, takes in player and dungeon and let the player
        play in the dungeon! :)
        """

        self.view.print_game(player, dungeon, View.direction_option)
        while True:
            if player.hp < 1:
                break

            if player.AI is True:
                if player.current_room.position[0] > player.destination.position[0]:
                    print("going west")
                    inp = "w"
                elif player.current_room.position[0] < player.destination.position[0]:
                    print("going east")
                    inp = "e"
                elif player.current_room.position[1] > player.destination.position[1]:
                    print("going north")
                    inp = "n"
                elif player.current_room.position[1] < player.destination.position[1]:
                    print("going south")
                    inp = "s"
                else:
                    print("go find", player.destination.position)
                    inp = "lolrandum"
            else:
                inp = self.view.handle_input()
            # inp = self.view.handle_input()

            new_room = player.move_character(inp, dungeon)
            if new_room is False:
                self.view.print_game(player,
                                     dungeon,
                                     View.direction_option,
                                     View.err_choice,
                                     error=True)
            else:
                self.view.print_game(player,
                                     dungeon,
                                     View.direction_option)

            if player.current_room.hasExit is True:
                self.view.print_game(player,
                                     dungeon,
                                     View.leave_question)
            while len(player.current_room.monsters) > 0:
                for monster in player.current_room.monsters:
                    self.view.print_game(player,
                                         dungeon,
                                         View.show_monsters,
                                         monster.unit_type,
                                         foes=True)
                time.sleep(3)
                while len(player.current_room.monsters) > 0:
                    self.combat(player, dungeon)
            while len(player.current_room.treasures) > 0:
                # Not as intended
                self.view.print_game(player,
                                     dungeon,
                                     View.score_text,
                                     player.score,
                                     score=True)

    def loot(self, player):
        """
        Returns a list of looted items to be displayed for the user
        """
        looted = []
        for loot in player.current_room.treasures:
            player.score = int(player.score)
            player.score += loot.value
            player.current_room.treasures.pop(0)
            looted.append(loot.item_type)
        return looted

    def combat(self, player, dungeon):
        """
        Takes in player and dungeon
        Runs combats and returns true or false
        SUGGESTION: RETURNS WON, ESCAPED OR LOST
        """
        initiative_list = []
        monster = player.current_room.monsters[0]
        player_init = player.roll_dice("initiative")
        monster_init = monster.roll_dice("initiative")
        if player.special_ability == "block":
            player.block = True
        if monster_init > player_init:
            initiative_list.append(monster)
            initiative_list.append(player)
        else:
            initiative_list.append(player)
            initiative_list.append(monster)
        while len(initiative_list) > 1:
            for actor in initiative_list:
                if player.hp < 1:
                    self.view.print_game(player,
                                         dungeon,
                                         View.player_dead,
                                         monster.unit_type,
                                         killed_by=True)
                    time.sleep(5)
                    initiative_list = []
                    player.current_room.monsters.clear()
                    return False

                if monster.hp < 1:
                    self.view.print_game(player,
                                         dungeon,
                                         View.player_killed,
                                         monster.unit_type,
                                         killed=True)
                    initiative_list = []
                    player.current_room.monsters.pop(0)
                    break
                elif isinstance(actor, Player):
                    while True:
                        self.view.print_game(player,
                                             dungeon,
                                             View.attack_options,
                                             monster.unit_type,
                                             monster=True)
                        if actor.AI is True:
                            choice = "1"
                        else:
                            choice = self.view.handle_input()
                        if choice == "1":
                            actor.attack_function(monster)
                            break
                        elif choice == "2":
                            escape = player.escape_combat()
                            if escape:
                                player.current_room = player.old_room
                                self.view.print_game(player,
                                                     dungeon,
                                                     View.player_escaped)
                                time.sleep(3)
                                initiative_list.clear()
                                return False
                            else:
                                self.view.print_game(player,
                                                     dungeon,
                                                     View.player_failed_escape)
                                break
                else:
                    actor.attack_function(player)
        return True
