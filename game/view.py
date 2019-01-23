import os
import platform


class View:

    welcome_menu = ["Welcome to... DUNGEON RUN!",
                    "[1] New Character",
                    "[2] Load Character",
                    "[3] Load AI Character",
                    "[4] Highest score",
                    "[5] Quit"]

    start_location = ["Choose your starting location:",
                      "[1] North-West",
                      "[2] North-East",
                      "[3] South-West",
                      "[4] South-East"]

    choose_role = ["Please choose your role:",
                   "[1] Knight",
                   "[2] Wizard",
                   "[3] Thief"]

    choose_size = ["Please choose your mapsize:",
                   "[1] 4x4",
                   "[2] 5x5",
                   "[3] 8x8"]

    choose_AI = ["Please choose AI:",
                 "[1] AI Knight",
                 "[2] AI Wizard",
                 "[3] AI Thief"]

    highscore = ["Display highscore:",
                 "number 1 is me",
                 "number 2 is you",
                 "number 3 is some other dude"]

    choose_corner = ["Choose your starting location:",
                     "[1] North-West",
                     "[2] North-East",
                     "[3] South-West",
                     "[4] South-East"]

    direction_option = ["        [N] North      ",
                        "[W] West          [E] East",
                        "        [S] South      "]

    attack_options = ["[1] Attack!",
                      "[2] Flee!"]

    leave_options = ["[1] Yes",
                     "[2] No"]

    good_bye = ["Thanks for playing!", "", "/Sonsofbjorn"]

    enter_go_back = ["", "", "[ENTER] to return."]

    stats_count = ["", "---- Killed Monsters ----",
                   "Giant Spider: ",
                   "Skeletons: ",
                   "Orcs: ",
                   "Troll: ",
                   "",
                   "Tresure count: ", "Total Score: ", "", "", ""]

    enter_char_name = ["", "Enter character name: ", "", "", "", "", "", "Type 'back' to return"]

    leave_question = ["You see a staircaise,", "do you want to leave?"]

    show_monsters = ["Uhuh! ENEMIES! You see the following foes: "]

    player_is_dead = ["", "Character has died and cannot be played!"]
    score_text = ["Your current score is: "]
    loot_text = ["You found loot! The following loot was added to your backback: "]
    player_dead = ["You have been slained by the"]
    player_killed = ["You have slain the "]
    player_escaped = ["You have escaped!"]
    player_failed_escape = ["You have failed to escape!"]
    player_hit = ["You hit the"]
    monster_hit = ["You have been hit by the"]
    for_one_dmg = ["for 1 damage"]
    player_miss = ["You missed"]
    monster_miss = ["Missed!"]
    player_crit = [" You did a critical hit to "]
    shield_block = ["Your shield blocked the attack from  "]
    hit = [" hit "]
    you_died = ["You have died!", "All your loot this round was lost", "and not added to your highscore", "", "[ENTER] to return"]
    exit_score = ["The score has been added to your highscore!"]

    """ ERROR MESESAGES BELLOW """
    error_msg = []
    err_choice = ["", "Invalid choice!"]
    err_long_name = ["", "Max 18 characters!"]
    err_invalid_char = ["", "Invalid character ','"]
    err_player_exists = ["", "Player name is taken"]
    err_player_not_exist = ["", "Player does not exist"]
    err_load_error = ["", "Load error, ask Micke"]
    """ END OF ERROR MESSAGES"""

    """ COLOR DICTIONARY BELOW"""
    colors = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m"
    }

    def clear_console(self):
        if platform.system() == "Linux":
            return os.system('clear')
        if platform.system() == "Darwin":
            return os.system('clear')
        elif platform.system() == "Windows":
            return os.system('cls')

    def draw_map(self, player, dungeon):
        """
        This takes in player and dungeon object
        Returns a list with the map and player loc
        """
        output = []
        outrow = ""
        for row in dungeon:
            for n in range(3):
                for room in row:
                    if room.position == player.show_location:
                        if n == 0 and len(room.get_room_monsters()) > 1:
                            out = "░M░░░░"
                        elif n == 0 and len(room.get_room_monsters()) == 1:
                            out = "░m░░░░"
                        elif n == 1:
                            out = "░░╳░░░"
                        else:
                            out = "░░░░░░"
                    elif room.has_exit and room.is_dark is False:
                        if n == 0 and len(room.get_room_monsters()) > 1:
                            out = "░M░░░░"
                        elif n == 0 and len(room.get_room_monsters()) == 1:
                            out = "░m░░░░"
                        if n == 1:
                            out = "░EXIT░"
                        else:
                            out = "░░░░░░"
                    elif not room.is_dark and len(room.get_room_monsters()) > 0:
                        if n == 0 and len(room.get_room_monsters()) > 1:
                            out = "░M░░░░"
                        elif n == 0 and len(room.get_room_monsters()) == 1:
                            out = "░m░░░░"
                        else:
                            out = "░░░░░░"
                    elif room.is_dark:
                        out = "▓▓▓▓▓▓"
                    else:
                        out = "░░░░░░"
                    outrow += out
                output.append(outrow)
                outrow = ""
        return output

    def print_main_menu(self, input_menu, *args, **kwargs):
        """
        Prints main menu, takes in *args which can be list, or strings and
        will be printed as the menu.
        **kwargs is a keyword argument if you want to show extra information,
        you will then send in an extra string/list.
        """
        self.clear_console()
        print("\033[31m"+"______                                                              ".center(os.get_terminal_size().columns))
        print("|  _  \                                                             ".center(os.get_terminal_size().columns))
        print("| | | | _   _  _ __    __ _   ___   ___   _ __   _ __  _   _  _ __  ".center(os.get_terminal_size().columns))
        print("| | | || | | || '_ \  / _` | / _ \ / _ \ | '_ \ | '__|| | | || '_ \ ".center(os.get_terminal_size().columns))
        print("| |/ / | |_| || | | || (_| ||  __/| (_) || | | || |   | |_| || | | |".center(os.get_terminal_size().columns))
        print("|___/   \__,_||_| |_| \__, | \___| \___/ |_| |_||_|    \__,_||_| |_|".center(os.get_terminal_size().columns))
        print("\033[32m"+"         ╔═════════════\033[31m __/ | \033[32m══════════════════════════════╗        ".center(os.get_terminal_size().columns+10), end="")
        print("        ║             \033[31m|___/\033[32m                                ║        ".center(os.get_terminal_size().columns+10))
        print("        ║                                                  ║        ".center(os.get_terminal_size().columns))
        print("        ║                                                  ║        ".center(os.get_terminal_size().columns))
        print("        ║                                                  ║        ".center(os.get_terminal_size().columns))

        menu = []

        if isinstance(input_menu, str) or not hasattr(input_menu, "__iter__"):
            menu.append(input_menu)
        else:
            menu = input_menu.copy()

        if kwargs:
            if isinstance(args[0], str) or not hasattr(args[0], "__iter__"):
                to_list = list()
                to_list.append(args[0])
            else:
                to_list = args[0]
            menu += to_list
        for row in menu:
            row = ("║"+row.center(50)+"║")
            print(row.center(os.get_terminal_size().columns))

        if len(menu) < 10:
            count = 10 - len(menu)
            for i in range(count):
                hehe1 = ("║"+" "*50+"║")
                print(hehe1.center(os.get_terminal_size().columns))
        print("╚══════════════════════════════════════════════════╝".center(os.get_terminal_size().columns))
        menu = []

    def print_game(self, player, dungeon, input_menu, *args, **kwargs):
        """
        This prints all the GFX for the game loop.
        Needs player object, dungeon and a menu list. Use *args and **kwargs
        to display extra information addition to the menu list.

        *args = an extra list of information we want to display
        **kwargs = is a keyword boolean and should be true if we want to
        show extra info.
        """

        self.clear_console()
        print("{red} ______                                                              ".format(red=self.colors.get("red")).center(os.get_terminal_size().columns+5))
        print("|  _  \                                                             ".center(os.get_terminal_size().columns))
        print("| | | | _   _  _ __    __ _   ___   ___   _ __   _ __  _   _  _ __  ".center(os.get_terminal_size().columns))
        print("| | | || | | || '_ \  / _` | / _ \ / _ \ | '_ \ | '__|| | | || '_ \ ".center(os.get_terminal_size().columns))
        print("| |/ / | |_| || | | || (_| ||  __/| (_) || | | || |   | |_| || | | |".center(os.get_terminal_size().columns))
        print("|___/   \__,_||_| |_| \__, | \___| \___/ |_| |_||_|    \__,_||_| |_|".center(os.get_terminal_size().columns))
        print("{green}   ╔══════════════════{red} __/ | {green}═══════════════════════════════════╗   ".format(red=self.colors.get("red"), green=self.colors.get("green")).center(os.get_terminal_size().columns+16), end="")
        print("   ║                  {red}|___/{green}                                     ║   ".format(red=self.colors.get("red"), green=self.colors.get("green")).center(os.get_terminal_size().columns+8))
        print("   ║                            MAP   m = One monster           ║   ".center(os.get_terminal_size().columns))
        print("   ║       ╳ = YOUR LOCATION          M = More than one monster ║   ".center(os.get_terminal_size().columns))
        playerbox = self.print_hp_score_list(player)
        monsterbox = self.print_monster_hp(player)
        playerbox_cursor = 0
        monsterbox_cursor = 0
        dungeonmap = self.draw_map(player, dungeon)
        if len(dungeonmap) < 13:
            for x in range(6):
                if len(player.current_room.monsters) > 0:
                    formated_output = (monsterbox[monsterbox_cursor]+"║" + " " * 60 + "║"+playerbox[playerbox_cursor])
                    if playerbox_cursor % 2 == 0:
                        print(formated_output.center(os.get_terminal_size().columns), end="")
                        playerbox_cursor += 1
                        monsterbox_cursor += 1
                    else:
                        print(formated_output.center(os.get_terminal_size().columns))
                        playerbox_cursor += 1
                        monsterbox_cursor += 1
                else:
                    formated_output = ("║" + " " * 60 + "║" + playerbox[playerbox_cursor])
                    if playerbox_cursor % 2 == 0:
                        print(formated_output.center(os.get_terminal_size().columns+22), end="")
                        playerbox_cursor += 1
                        monsterbox_cursor += 1
                    else:
                        print(formated_output.center(os.get_terminal_size().columns-22))
                        playerbox_cursor += 1
                        monsterbox_cursor += 1
            for row in dungeonmap:
                if playerbox_cursor < 16 and monsterbox_cursor < 8 and len(player.current_room.monsters) > 0:
                    row = (monsterbox[monsterbox_cursor] + "║" + row.center(60) + "║" + playerbox[playerbox_cursor])
                    if playerbox_cursor == 6:
                        print(row.center(os.get_terminal_size().columns+20), end="")
                    elif playerbox_cursor % 2 == 0:
                        print(row.center(os.get_terminal_size().columns), end="")
                    else:
                        print(row.center(os.get_terminal_size().columns))
                elif playerbox_cursor < 16:
                    row = ("║" + row.center(60) + "║" + playerbox[playerbox_cursor])
                    if playerbox_cursor == 6:
                        print(row.center(os.get_terminal_size().columns+32), end="")
                    elif playerbox_cursor % 2 == 0:
                        print(row.center(os.get_terminal_size().columns + 22), end="")
                    else:
                        print(row.center(os.get_terminal_size().columns - 22))
                else:
                    row = ("║" + row.center(60) + "║")
                    print(row.center(os.get_terminal_size().columns))
                monsterbox_cursor += 1
                playerbox_cursor += 1
        elif len(dungeonmap) < 16:
            for x in range(4):
                if len(player.current_room.monsters) > 0:
                    formated_output = (monsterbox[monsterbox_cursor]+"║" + " " * 60 + "║"+playerbox[playerbox_cursor])
                    if playerbox_cursor % 2 == 0:
                        print(formated_output.center(os.get_terminal_size().columns), end="")
                        playerbox_cursor += 1
                        monsterbox_cursor += 1
                    else:
                        print(formated_output.center(os.get_terminal_size().columns))
                        monsterbox_cursor += 1
                        playerbox_cursor += 1
                else:
                    formated_output = ("║" + " " * 60 + "║" + playerbox[playerbox_cursor])
                    if playerbox_cursor % 2 == 0:
                        print(formated_output.center(os.get_terminal_size().columns + 22), end="")
                        playerbox_cursor += 1
                        monsterbox_cursor += 1
                    else:
                        print(formated_output.center(os.get_terminal_size().columns - 22))
                        monsterbox_cursor += 1
                        playerbox_cursor += 1
            for row in dungeonmap:
                if playerbox_cursor < 16 and monsterbox_cursor < 8 and len(player.current_room.monsters) > 0:
                    row = (monsterbox[monsterbox_cursor]+"║"+row.center(60)+"║"+playerbox[playerbox_cursor])
                    if playerbox_cursor == 6:
                        print(row.center(os.get_terminal_size().columns+20), end="")
                    elif playerbox_cursor % 2 == 0:
                        print(row.center(os.get_terminal_size().columns), end="")
                    else:
                        print(row.center(os.get_terminal_size().columns))
                elif playerbox_cursor < 16:
                    row = ("║" + row.center(60) + "║" + playerbox[playerbox_cursor])
                    if playerbox_cursor == 6:
                        print(row.center(os.get_terminal_size().columns+32), end="")
                    elif playerbox_cursor % 2 == 0:
                        print(row.center(os.get_terminal_size().columns + 22), end="")
                    else:
                        print(row.center(os.get_terminal_size().columns - 22))
                else:
                    row = ("║" + row.center(60) + "║")
                    print(row.center(os.get_terminal_size().columns))
                monsterbox_cursor += 1
                playerbox_cursor += 1

        elif len(dungeonmap) > 16:
            for row in dungeonmap:
                if playerbox_cursor < 16 and monsterbox_cursor < 8 and len(player.current_room.monsters) > 0:
                    row = (monsterbox[monsterbox_cursor]+"║"+row.center(60)+"║"+playerbox[playerbox_cursor])
                    if playerbox_cursor == 6:
                        print(row.center(os.get_terminal_size().columns+20), end="")
                    elif playerbox_cursor % 2 == 0:
                        print(row.center(os.get_terminal_size().columns), end="")
                    else:
                        print(row.center(os.get_terminal_size().columns))
                elif playerbox_cursor < 16:
                    row = ("║" + row.center(60) + "║" + playerbox[playerbox_cursor])
                    if playerbox_cursor == 6:
                        print(row.center(os.get_terminal_size().columns+32), end="")
                    elif playerbox_cursor % 2 == 0:
                        print(row.center(os.get_terminal_size().columns + 22), end="")
                    else:
                        print(row.center(os.get_terminal_size().columns - 22))
                else:
                    row = ("║" + row.center(60) + "║")
                    print(row.center(os.get_terminal_size().columns))
                monsterbox_cursor += 1
                playerbox_cursor += 1
        if len(dungeonmap) < 13:
            for x in range(6):
                formated_output = ("║" + " " * 60 + "║")
                print(formated_output.center(os.get_terminal_size().columns))
        elif len(dungeonmap) < 16:
            for x in range(5):
                formated_output = ("║" + " " * 60 + "║")
                print(formated_output.center(os.get_terminal_size().columns))
        print("   ║                                                            ║   ".center(os.get_terminal_size().columns))
        print("   ║                                                            ║   ".center(os.get_terminal_size().columns))
        print("╚════════════════════════════════════════════════════════════╝".center(os.get_terminal_size().columns))
        print("   ╔════════════════════════════════════════════════════════════════════════════╗   ".center(os.get_terminal_size().columns))
        print("   ║                                                                            ║   ".center(os.get_terminal_size().columns))
        menu = []

        if isinstance(input_menu, str) or not hasattr(input_menu, "__iter__"):
            menu.append(input_menu)
        else:
            menu = input_menu.copy()

        if kwargs:
            if isinstance(args[0], str) or not hasattr(args[0], "__iter__"):
                to_list = list()
                to_list.append(args[0])
            else:
                to_list = args[0]
            menu += to_list

        for row in menu:
            row = ("║"+row.center(76)+"║")
            print(row.center(os.get_terminal_size().columns))
        for i in range(5-len(menu)):
            extralines = ("║" + " " * 76 + "║")
            print(extralines.center(os.get_terminal_size().columns))
        print("   ╚════════════════════════════════════════════════════════════════════════════╝   ".center(os.get_terminal_size().columns))

    def print_hp_score_list(self, player):
        losthp = player.max_hp - int(player.hp)
        hpbar = "{red}".format(red=self.colors.get("red"))+("▒"*int(losthp))+"{green}".format(green=self.colors.get("green"))+("▓"*int(player.hp))
        hp_score_list = (" ╔══════════════════╗",
                         " ║       NAME:      ║",
                         " ║"+player.name.center(18)+"║",
                         " ╚══════════════════╝",
                         " ╔══════════════════╗",
                         " ║        HP:       ║",
                         " ║"+hpbar.center(28)+"║",
                         " ╚══════════════════╝",
                         " ╔══════════════════╗",
                         " ║      CLASS:      ║",
                         " ║"+player.hero_class.center(18) + "║",
                         " ╚══════════════════╝",
                         " ╔══════════════════╗",
                         " ║      SCORE:      ║",
                         " ║"+str(player.score).center(18)+"║",
                         " ╚══════════════════╝"
                         )
        return hp_score_list

    def print_monster_hp(self, player):
        if len(player.current_room.monsters) > 0:
            monster_hp = player.current_room.monsters[0].hp
            monster_max_hp = player.current_room.monsters[0].max_hp
            losthp = int(monster_max_hp) - int(monster_hp)
            hpbar = "{red}".format(red=self.colors.get("red"))+("▒" * int(losthp))+"{green}".format(green=self.colors.get("green")) + ("▓" * int(monster_hp))
            hp_score_list = (" ╔══════════════════╗ ",
                             " ║     MONSTER:     ║ ",
                             " ║" + player.current_room.monsters[0].unit_type.center(18) + "║ ",
                             " ╚══════════════════╝ ",
                             " ╔══════════════════╗ ",
                             " ║    MONSTER HP:   ║ ",
                             " ║" + hpbar.center(28) + "║ ",
                             " ╚══════════════════╝ "
                             )
        else:
            hp_score_list = ()
        return hp_score_list


    def center_text(self, text):
        print(text.center(os.get_terminal_size().columns))

    def handle_input(self):
        return input("Choice: ".rjust(os.get_terminal_size().columns//2))
