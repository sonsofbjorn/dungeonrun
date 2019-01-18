import os
import platform


class View:

    welcome_menu = ["Welcome to... DUNGEON RUN!",
                    "[1] New Character",
                    "[2] Load Character",
                    "[3] Highest score",
                    "[4] Quit"]

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

    good_bye = ["Thanks for playing!", "", "/Sonsofbjorn"]

    enter_char_name = ["", "Enter character name: "]

    leave_question = ["You see a staircaise,", "do you want to leave?"]

    show_monsters = ["Uhuh! ENEMIES! You see the following foes: ", ""]
    score_text = ["Your current score is: "]
    loot_text = ["You found loot! The following loot was added to your backback: "]
    player_dead = ["You have been slained by: "]
    player_killed = ["You have slain the: "]
    player_escaped = ["You have escaped!"]
    player_failed_escape = ["You have failed to escape!"]

    """ ERROR MESESAGES BELLOW """
    error_msg = []
    err_choice = ["", "Invalid choice!"]
    err_long_name = ["", "Max 18 characters!"]
    err_invalid_char = ["", "Invalid character ','"]
    err_player_exists = ["", "Player name is taken"]
    err_player_not_exist = ["", "Player does not exist"]
    err_load_error = ["", "Load error, ask Micke"]
    """ END OF ERROR MESSAGES"""

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
                        if n == 1:
                            out = "░░╳░░░"
                        else:
                            out = "░░░░░░"
                    elif room.hasExit and room.dark is False:
                        out = "░EXIT░"
                    elif room.dark:
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
        print("______                                                              ".center(os.get_terminal_size().columns))
        print("|  _  \                                                             ".center(os.get_terminal_size().columns))
        print("| | | | _   _  _ __    __ _   ___   ___   _ __   _ __  _   _  _ __  ".center(os.get_terminal_size().columns))
        print("| | | || | | || '_ \  / _` | / _ \ / _ \ | '_ \ | '__|| | | || '_ \ ".center(os.get_terminal_size().columns))
        print("| |/ / | |_| || | | || (_| ||  __/| (_) || | | || |   | |_| || | | |".center(os.get_terminal_size().columns))
        print("|___/   \__,_||_| |_| \__, | \___| \___/ |_| |_||_|    \__,_||_| |_|".center(os.get_terminal_size().columns))
        print("        ╔═════════════ __/ | ══════════════════════════════╗        ".center(os.get_terminal_size().columns))
        print("        ║             |___/                                ║        ".center(os.get_terminal_size().columns))
        print("        ║                                                  ║        ".center(os.get_terminal_size().columns))
        print("        ║                                                  ║        ".center(os.get_terminal_size().columns))
        print("        ║                                                  ║        ".center(os.get_terminal_size().columns))

        menu = []
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
        nameprint = ("    ║ ╳ = your location"+"".center(42)+""+"║ ║"+player.name.center(18)+"║  ")
        print("______                                                              ".center(os.get_terminal_size().columns))
        print("|  _  \                                                             ".center(os.get_terminal_size().columns))
        print("| | | | _   _  _ __    __ _   ___   ___   _ __   _ __  _   _  _ __  ".center(os.get_terminal_size().columns))
        print("| | | || | | || '_ \  / _` | / _ \ / _ \ | '_ \ | '__|| | | || '_ \ ".center(os.get_terminal_size().columns))
        print("| |/ / | |_| || | | || (_| ||  __/| (_) || | | || |   | |_| || | | |".center(os.get_terminal_size().columns))
        print("|___/   \__,_||_| |_| \__, | \___| \___/ |_| |_||_|    \__,_||_| |_|".center(os.get_terminal_size().columns))
        print("   ╔══════════════════ __/ | ═══════════════════════════════════╗ ╔══════════════════╗  ".center(os.get_terminal_size().columns+20), end="")
        print("   ║                  |___/     MAP                             ║ ║       NAME:      ║  ".center(os.get_terminal_size().columns-20))
        print(nameprint.center(os.get_terminal_size().columns+20), end="")
        print("   ║                                                            ║ ╚══════════════════╝  ".center(os.get_terminal_size().columns-20))
        sidebox = self.print_hp_score_list(player)
        a = 0
        dungeonmap = self.draw_map(player, dungeon)
        for row in dungeonmap:
            if a < 8:
                row = ("║"+row.center(60)+"║"+sidebox[a])
                if a % 2 == 0:
                    print(row.center(os.get_terminal_size().columns+22), end="")
                else:
                    print(row.center(os.get_terminal_size().columns-22))
            else:
                row = ("║" + row.center(60) + "║")
                print(row.center(os.get_terminal_size().columns))
            a += 1
        if len(dungeonmap) < 10:
            count = 10 - len(dungeonmap)
            for i in range(count):
                hehe1 = ("║"+" "*60+"║")
                print(hehe1.center(os.get_terminal_size().columns))
        print("   ║                                                            ║   ".center(os.get_terminal_size().columns))
        print("   ║                                                            ║   ".center(os.get_terminal_size().columns))
        print("╚════════════════════════════════════════════════════════════╝".center(os.get_terminal_size().columns))
        print("   ╔════════════════════════════════════════════════════════════════════════════╗   ".center(os.get_terminal_size().columns))
        print("   ║                                                                            ║   ".center(os.get_terminal_size().columns))
        menu = []
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
        for i in range(10):
            extralines = ("║" + " " * 76 + "║")
            print(extralines.center(os.get_terminal_size().columns))
        print("   ╚════════════════════════════════════════════════════════════════════════════╝   ".center(os.get_terminal_size().columns))

    def print_hp_score_list(self, player):
        hp_score_list = (" ╔══════════════════╗",
                         " ║        HP:       ║",
                         " ║"+str(player.hp).center(18)+"║",
                         " ╚══════════════════╝",
                         " ╔══════════════════╗",
                         " ║      SCORE:      ║",
                         " ║"+str(player.score).center(18)+"║",
                         " ╚══════════════════╝"
                         )
        return hp_score_list

    def center_text(self, text):
        print(text.center(os.get_terminal_size().columns))

    def handle_input(self):
        return input()
