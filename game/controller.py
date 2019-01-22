from view import View
from player import Player
from dungeon import Map
import time
import random


class Controller:
    def __init__(self):
        self.view = View()
        self.killed_monsters = []
        self.looted_items = []

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
                    if player_name == "back":
                        self.main_menu()
                    elif self.player_exists(player_name):
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
                self.view.print_main_menu(self.get_top_highschores(), View.enter_go_back, error=True)
                self.view.handle_input()  # ENTER TO CONTINUE
                self.main_menu()

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
                self.view.print_main_menu(View.choose_size,
                                          View.err_choice,
                                          error=True)
                time.sleep(3)
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
                self.view.print_main_menu(View.choose_corner,
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

            if usr_choice == "back":
                self.main_menu()

            elif len(usr_choice) >= 18:
                self.view.print_main_menu(View.enter_char_name,
                                          View.err_long_name,
                                          error=True)
            elif ',' in usr_choice:
                self.view.print_main_menu(View.enter_char_name,
                                          View.err_invalid_char,
                                          error=True)
            elif len(usr_choice) == 0:
                self.view.print_main_menu(View.enter_char_name,
                                          View.err_choice,
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
        '''
        This function checks if a player is already in the players.txt.
        :param uname: Takes a name as an aragument to check versus a file
        :return: returns True if player exists or False if it doesnt exists
        '''
        with open("players.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, score, highscore) = line.split(sep=",")
                if username == uname.capitalize():
                    return True, uname
        return False

    def player_killed(self, player):
        with open("players.txt", "r") as f:
            lines = f.readlines()
        count = 0
        pos = 0
        for row in lines:
            if row.startswith(player.name):
                (username, role, dead, highscore) = row.split(sep=",")
                pos = count
            count += 1
        lines[pos] = player.name+","+player.hero_class+","+"1"+","+highscore
        print(lines)
        with open("players.txt", "w") as f:
            f.writelines(lines)

    def is_player_dead(self, player):
        with open("players.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, dead, highscore) = line.split(sep=",")
                if username == player.name.capitalize():
                    if dead == "1":
                        return True
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

    def update_player_score(self, player):
        with open("players.txt", "r") as f:
            lines = f.readlines()
        count = 0
        pow = 0
        for row in lines:
            if row.startswith(player.name):
                (username, role, dead, highscore) = row.split(sep=",")
                pos = count
            count += 1
        newscore = player.score+int(highscore)
        lines[pos] = player.name+","+player.hero_class+","+"0"+","+str(newscore)+"\n"
        with open("players.txt", "w") as f:
            f.writelines(lines)

    def get_top_highschores(self):
        """
        This function reads players.txt and returns a list
        of strings for the top 5 players
        """
        scores = []
        filename = "players.txt"
        with open(filename, mode="r") as f:
            for line in f:
                x = line.split(',')
                scores.append("{:006d}{:>20s}".format(int(x[-1]), x[0]))
            scores.sort()
            scores.append('~ H I G H S C O R E ~')
            scores.reverse()
        return scores[:6]

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

    def generate_exit(self, dungeon_size, dungeon, start_room):
        '''
        This will generate an exit
        It will generate a new exit if the 
        location is the same as the player
        start_room
        '''
        while(True):

            rand_x = random.randint(0, dungeon_size-1)
            rand_y = random.randint(0, dungeon_size-1)
            exit_room = dungeon.get_room(rand_x, rand_y)

            if exit_room is not start_room:
                exit_room.has_exit = True
                break

    def init_objects(self, player, role, start_loc,
                     dungeon_size, ai_check=False):
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
        elif start_loc == "NE":
            start_room = dungeon.corner["NE"]
        elif start_loc == "SW":
            start_room = dungeon.corner["SW"]
        elif start_loc == "SE":
            start_room = dungeon.corner["SE"]

        player = Player(player, role, start_room)
        self.generate_exit(dungeon_size, dungeon, start_room)

        if ai_check is True:
            player.ai = True
            player.start_room = start_room
            self.ai_find_exit(player, dungeon)
        player.current_room.monsters = []
        player.current_room.treasures = []
        player.current_room.is_dark = False

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

        while True:
            self.view.print_game(player, dungeon, View.direction_option)

            direction = self.view.handle_input()
            # inp = self.view.handle_input()
            # ASK PLAYER DIRECTION
            new_room = self.move_player(player, direction, dungeon)

            if new_room is False:
                self.view.print_game(player,
                                     dungeon,
                                     View.direction_option,
                                     View.err_choice,
                                     error=True)
                time.sleep(2)
            else:
                self.view.print_game(player,
                                     dungeon,
                                     View.direction_option)

            if player.current_room.has_exit is True:
                while True:
                    self.view.print_game(player,
                                        dungeon,
                                        View.leave_question,
                                        View.leave_options,
                                        leave_q=True)
                    usrinp = self.view.handle_input()
                    if usrinp == "1":
                        self.statistics(player)
                        time.sleep(3)
                        quit()
                    if usrinp == "2":
                        break
                    else:
                        self.view.print_game(player,
                                            dungeon,
                                            View.leave_question,
                                            View.err_choice,
                                            error=True)
                    time.sleep(2)
            while len(player.current_room.monsters) > 0:
                self.view.print_game(player,
                                     dungeon,
                                     View.show_monsters,
                                     player.current_room.get_room_monsters(),
                                     foes=True)
                time.sleep(3)
                while len(player.current_room.monsters) > 0:
                    self.combat(player, dungeon)

            if player.hp < 1:
                self.player_killed(player)
                self.statistics(player)

            while len(player.current_room.treasures) > 0:
                self.loot(player, dungeon)

    def statistics(self, player):
        results = []
        results = View.stats_count.copy()

        # RESULTS [1] KILLED
        # RESULTS [2] TREASURES
        # RESULT [3] TOTAL SCORE
        if not self.is_player_dead(player):
            self.update_player_score(player)
            results[1] += str(len(self.killed_monsters))
            results[2] += str(len(self.looted_items))
            results[3] += str(player.score)
            results[4] = "You scored a new highscore!"
            results[6] = View.enter_go_back[2]

            self.view.print_main_menu(View.good_bye,
                                      results,
                                      end=True)
        else:
            self.view.print_main_menu(View.good_bye,
                                      View.you_died,
                                      end=True)
        usr_input = self.view.handle_input()
        self.main_menu()

    def loot(self, player, dungeon):
        """
        Returns a list of looted items to be displayed for the user
        """
        looted = []
        for loot in player.current_room.treasures:
            player.score = int(player.score)
            player.score += loot.value
            self.looted_items.append(player.current_room.treasures.pop(0))
            looted.append(loot.item_type)
            self.view.print_game(player,
                                 dungeon,
                                 View.loot_text,
                                 loot.item_type,
                                 loot=True)
            time.sleep(3)

        return looted

    def combat(self, player, dungeon):
        """
        Takes in player and dungeon
        Runs combats and returns true or false
        SUGGESTION: RETURNS WON, ESCAPED OR LOST
        """
        initiative_list = []
        monster = player.current_room.monsters[0]
        player_init = self.roll_dice(player, "initiative")
        monster_init = self.roll_dice(monster, "initiative")
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
                    time.sleep(3)
                    initiative_list = []
                    self.killed_monsters.append(player.current_room.monsters.pop(0))
                    if player.special_ability == "block":
                        player.block = True
                    break
                elif isinstance(actor, Player):
                    while True:
                        self.view.print_game(player,
                                             dungeon,
                                             View.attack_options,
                                             monster.unit_type,
                                             monster=True)
                        if actor.ai is True:
                            choice = "1"
                        else:
                            choice = self.view.handle_input()
                        if choice == "1":
                            result = self.attack_function(actor, monster)
                            self.view.print_game(player,
                                                 dungeon,
                                                 *result,
                                                 show_result=True)
                            time.sleep(2)
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
                                time.sleep(3)
                                break
                else:
                    result = self.attack_function(actor, player)
                    self.view.print_game(player,
                                         dungeon,
                                         *result,
                                         show_result=True)
                    time.sleep(2)
        return True

    def move_player(self, player, direction, dungeon_map):
        """
        This moves a player object on the map
        with directions, N, E, S, W as strings
        It then returns a new room object.
        If the player fails in moving it returns
        a False
        """
        x = player.current_room.position[0]
        y = player.current_room.position[1]

        direction = direction.upper()[:1]

        while True:
            if player.current_room.doors.get(direction) is False:
                return False
            else:
                break

        if direction == "W":
            new_room = dungeon_map.get_room(x-1, y)
        elif direction == "N":
            new_room = dungeon_map.get_room(x, y-1)
        elif direction == "E":
            new_room = dungeon_map.get_room(x+1, y)
        elif direction == "S":
            new_room = dungeon_map.get_room(x, y+1)
        else:
            return False
        new_room.is_dark = False
        player.old_room = player.current_room
        player.current_room = new_room

        return new_room

    def attack_function(self, attacker, defender):
        attacker_roll = self.roll_dice(attacker, "attack")
        defender_roll = self.roll_dice(defender, "dexterity")

        if attacker_roll > defender_roll:
            if isinstance(attacker, Player):
                if attacker.hero_class == "thief":
                    critical_hit = random.randrange(0, 100)
                    if critical_hit >= 75:
                        defender.hp -= 2
                        return attacker.name, View.player_crit, defender.unit_type
                    else:
                        defender.hp -= 1
                        return attacker.name, View.player_hit, defender.unit_type
                else:
                    defender.hp -= 1
                    return View.player_hit, defender.unit_type, View.for_one_dmg
            else:
                if defender.hero_class == "knight":
                    if defender.block is True:
                        defender.block = False
                        return View.shield_block, attacker.unit_type
                    else:
                        defender.hp -= 1
                        return View.monster_hit, attacker.unit_type, View.for_one_dmg
                else:
                    defender.hp -= 1
                    return View.monster_hit, attacker.unit_type, View.for_one_dmg
        else:
            if isinstance(attacker, Player):
                return View.player_miss, defender.unit_type
            else:
                return attacker.unit_type, View.monster_miss

    def roll_dice(self, user, dice_type):
        if dice_type == "attack":
            dice_type = user.attack
        elif dice_type == "dexterity":
            dice_type = user.dexterity
        elif dice_type == "initiative":
            dice_type = user.initiative
        value = 0
        for x in range(0, dice_type):
            value += random.randrange(0, dice_type)
        return value
