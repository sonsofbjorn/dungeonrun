from view import View
from player import Player
from dungeon import Map


class Controller:
    def __init__(self):
        print("something")
        self.d = Map(5)
        self.p = Player("bob", "knight", self.d.get_room(2, 3))
        self.view = View(self.d, self.p)

    def main_menu(self):
        self.view.print_start_menu(View.welcome_menu, False)


        while True:
            usr_choice = self.view.handle_input()
            if usr_choice == "1":
                self.view.print_start_menu(View.enter_char_name, False)
                while True:
                    usr_choice = self.view.handle_input()
                    if len(usr_choice) >= 18:
                        self.view.handle_error(View.err_long_name)
                        self.view.print_start_menu(View.enter_char_name, True)
                    elif ',' in usr_choice:
                        self.view.handle_error(View.err_invalid_char)
                        self.view.print_start_menu(View.enter_char_name, True)
                    elif self.player_exists(usr_choice):
                        self.view.handle_error(View.err_player_exists)
                        self.view.print_start_menu(View.enter_char_name, True)
                    else:
                        break
                break
            elif usr_choice == "2":
                self.view.print_start_menu(View.enter_char_name)
                break
            elif usr_choice == "3":
                self.view.print_start_menu(View.highscore)  # NOT IMPLEMENTED, REFACTOR TO FUNCTION
                break
            elif usr_choice == "4":
                self.view.print_start_menu(View.good_bye)
                quit()
            else:
                self.view.handle_error(View.err_choice)
                self.view.print_start_menu(View.welcome_menu, True)

    def player_exists(uname):
        with open("players.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, score, highscore) = line.split(sep=",")
                if username == uname.capitalize():
                    return True
        return False
