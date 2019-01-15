import os


class View:

    def __init__(self, dungeon, player):
        self.m = dungeon
        self.p = player

    def draw_map(self):
        tests = []
        for row in self.m:
            for x in range(3):
                for room in row:
                    if room.position == self.p.show_location:
                        if x == 1:
                            print(" ", end="")
                            print(" ╳  ", end="")
                            print(" ", end="")
                        else:
                            print("   ", end="")
                            print("", end="")
                            print("   ", end="")
                    elif room.hasExit and room.dark is False:
                        if x == 1:
                            print("░", end="")
                            print("exit", end="")
                            print("░", end="")
                        else:
                            print("░░░", end="")
                            print("", end="")
                            print("░░░", end="")

                    elif room.dark:
                        print("▓▓", end="")
                        print("▓▓", end="")
                        print("▓▓", end="")
                    else:
                        print("░░", end="")
                        print("░░", end="")
                        print("░░", end="")
                print()

    def print_it(self, text):
        os.system('cls')
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
        a = 0
        for i in range(len(text)):
            hehe = ("║"+text[a].center(50)+"║")
            print(hehe.center(os.get_terminal_size().columns))
            a += 1
        if len(text) < 10:
            count = 10 - len(text)
            for i in range(count):
                hehe1 = ("║"+" "*50+"║")
                print(hehe1.center(os.get_terminal_size().columns))
        print("╚══════════════════════════════════════════════════╝".center(os.get_terminal_size().columns))



    def center_text(self, text):
        print(text.center(os.get_terminal_size().columns))


    def test_list(self):
        optionlist = ("Choose your starting location:",
                      "[1] North-West",
                      "[2] North-East",
                      "[3] South-West",
                      "[4] South-East")
        return optionlist

    def start_menu_list(self):
        optionlist = ("Welcome to... DUNGEON RUN!",
                  "[1] New Character",
                  "[2] Load Character",
                  "[3] Remove Character",
                  "[4] Highest score",
                  "[5] Quit")
        return optionlist

    def draw_start_location_options(self):
        self.print_it(self.test_list())
        startcorner = input(">>")
        return startcorner

    def draw_map_loop(self):
        print(self.p.name + ", you are in", self.p.show_location)
        print(self.p.name + ", where do you want to go? West, North, East, or South?")
        inp = input(">>")
        return inp

