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

        while True:
            usr_choice = self.view.handle_input()
            if usr_choice == "1":
                if self.new_character():
                    break
            elif usr_choice == "2":
                self.view.print_start_menu(View.enter_char_name)
                break
            elif usr_choice == "3":
                self.view.print_start_menu(View.highscore)
                break
            elif usr_choice == "4":
                self.view.print_start_menu(View.good_bye)
                quit()
            else:
                #self.view.handle_error(View.err_choice)
                self.view.print_start_menu(View.welcome_menu,
                                           View.err_choice,
                                           error=True)

    def new_character(self):

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

        # character role
        while True:
            character_name = usr_choice
            self.view.print_start_menu(View.choose_role)
            usr_choice = self.view.handle_input()
            if usr_choice == "1":
                character_role = "knight"
                break
            elif usr_choice == "2":
                character_role = "wizard"
                break
            elif usr_choice == "3":
                character_role = "thief"
                break
            else:
                self.view.print_start_menu(View.choose_role,
                                           View.err_choice,
                                           error=True)

        # all done!
        self.save_player(character_name, character_role, 0, 0)
        return True

    def player_exists(uname):
        with open("players.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, score, highscore) = line.split(sep=",")
                if username == uname.capitalize():
                    return True
        return False

    def save_player(uname, role, score, highscore):
        with open("players.txt", "a+") as f:
            f.write(uname.capitalize()+","+role+","+str(score)+","+str(highscore)+"\n")

    def load_player(uname):
        with open("players.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, score, highscore) = line.split(sep=",")
                if username == uname.capitalize():
                    return username, role, score
        raise Exception("Something went wrong. What? No idea... Ask Sebbe")
