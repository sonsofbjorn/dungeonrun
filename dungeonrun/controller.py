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
        self.view.print_start_menu(View.welcome_menu)

        usr_choice = self.view.handle_input()

        while True:
            if usr_choice == "1":
                self.view.print_start_menu(View.enter_char_name)
                break
            elif usr_choice == "2":
                self.view.print_start_menu(View.enter_char_name)
            elif usr_choice == "3":
                self.view.print_start_menu(View.highscore)  # NOT IMPLEMENTED, REFACTOR TO FUNCTION
            elif usr_choice == "4":
                self.view.print_start_menu(View.good_bye)
                quit()
            else:
                self.view.print_start_menu(View.welcome_menu, View.error_msg)

    def player_exists(uname):
        with open("players.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, score, highscore) = line.split(sep=",")
                if username == uname.capitalize():
                    return True
        return False
