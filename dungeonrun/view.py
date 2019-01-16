import types
import os
import platform

class View:

    welcome_menu = ("Welcome to... DUNGEON RUN!",
                "[1] New Character",
                "[2] Load Character",
                "[3] Highest score",
                "[4] Quit")

    start_location = ("Choose your starting location:",
                  "[1] North-West",
                  "[2] North-East",
                  "[3] South-West",
                  "[4] South-East")

    enter_char_name = ("Enter character name: ")

    error_msg = ["\nNot a vavlid choice!\n"]

    def __init__(self, dungeon, player):
        self.m = dungeon
        self.p = player

    def clear_console(self):
        if platform.system() == "Linux" or "Darwin":
            return os.system('clear')
        elif platform.system() == "Windows":
            return os.system('cls')

    def draw_map2(self):
        output = []
        outrow = ""
        for row in self.m:
            for n in range(3):
                for room in row:
                    if room.position == self.p.show_location:
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

    def print_start_menu(self, menu, *err):
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
        for row in menu:
            row = ("║"+row.center(50)+"║")
            print(row.center(os.get_terminal_size().columns))

        error = ("║"+err(50)+"║")
        print(error.center(os.get_terminal_size().columns))
        if len(menu) < 10:
            count = 10 - len(menu)
            for i in range(count):
                hehe1 = ("║"+" "*50+"║")
                print(hehe1.center(os.get_terminal_size().columns))
        print("╚══════════════════════════════════════════════════╝".center(os.get_terminal_size().columns))

    def print_game(self, dungeonmap, menulist):
        self.clear_console()
        nameprint = ("    ║ ╳ = your location"+"".center(42)+""+"║ ║"+self.p.name.center(18)+"║  ")
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
        sidebox = self.print_hp_score_list()
        a = 0
        for row in dungeonmap:
            if a < 8:
                row = ("║"+row.center(60)+"║"+sidebox[a])
                if a%2 == 0:
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
        print("   ║                     HERE GOES ALL STRINGS FOR THE GAME                     ║   ".center(os.get_terminal_size().columns))
        for i in range(10):
            extralines = ("║" + " " * 76 + "║")
            print(extralines.center(os.get_terminal_size().columns))
        print("   ╚════════════════════════════════════════════════════════════════════════════╝   ".center(os.get_terminal_size().columns))

    def print_hp_score_list(self):

        hp_score_list = (" ╔══════════════════╗",
                         " ║        HP:       ║",
                         " ║"+str(self.p.hp).center(18)+"║",
                         " ╚══════════════════╝",
                         " ╔══════════════════╗",
                         " ║      SCORE:      ║",
                         " ║"+str(self.p.score).center(18)+"║",
                         " ╚══════════════════╝"
                         )
        return hp_score_list





    def center_text(self, text):
        print(text.center(os.get_terminal_size().columns))

    def draw_start_location_options(self):
        self.print_it(self.test_list())
        startcorner = input(">>")
        return startcorner

    def draw_map_loop(self):
        print(self.p.name + ", you are in", self.p.show_location)
        print(self.p.name + ", where do you want to go? West, North, East, or South?")
        inp = input(">>")
        return inp

    def handle_input(self):
        return input()
