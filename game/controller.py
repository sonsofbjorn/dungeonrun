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
                        if not self.is_player_dead(player_name.capitalize()):
                            player_tuple = self.load_player(player_name)
                            self.print_load_stats(*player_tuple)
                            dungeon_size = self.map_size_menu()
                            start_loc = self.start_loc_menu()
                            break
                        else:
                            self.view.print_main_menu(View.enter_char_name,
                                                      View.player_is_dead,
                                                      error=True)
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
            self.init_objects(*player_tuple[0:2], start_loc, dungeon_size, True)
        else:
            self.init_objects(*player_tuple[0:2], start_loc, dungeon_size)

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
        return random.choice([4, 5, 8])

    def start_loc_AI(self):
        return random.choice(["NW", "NE", "SW", "SE"])

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
        self.save_new_player(player_name, player_role)
        return player_name, player_role

    def player_exists(self, uname):
        '''
        This function checks if a player is already in the players.txt.
        :param uname: Takes a name as an aragument to check versus a file
        :return: returns True if player exists or False if it doesnt exists
        '''
        player_tuple = self.load_players_file(uname)
        if player_tuple is False:
            return False
        else:
            return True, player_tuple[0]

    def player_killed(self, player):
        '''
        Sets player to dead in text file
        :param uname: The argument is a player object
        :return: nothing
        '''
        with open("players.txt", "r") as f:
            lines = f.readlines()
        count = 0
        pos = 0
        for row in lines:
            if row.startswith(player.name):
                splits = row.split(sep=",")
                pos = count
            count += 1
        splits[2] = "1"
        lines[pos] = ",".join(splits)
        with open("players.txt", "w") as f:
            f.writelines(lines)

    def is_player_dead(self, uname):
        player_tuple = self.load_players_file(uname)
        if player_tuple[2] == "1":
            return True
        else:
            return False

    def save_new_player(self, uname, role):
        with open("players.txt", "a+") as f:
            f.write(uname.capitalize()
                    + ","+role+","+"0,0,0,0,0,0,0,0"+"\n")

    def load_player(self, uname):
        """
        This loads a player from players.txt
        Returns a tuple with name and role which will be used in init_objects
        """
        player_tuple = self.load_players_file(uname)
        return player_tuple

    def load_players_file(self, uname):
        with open("players.txt", "r") as f:
            file = f.readlines()
            for line in file:
                (username, role, dead, runs,
                 gs_killed, sk_killed, or_killed, tr_killed,
                 tres_collected, highscore) = line.split(sep=",")

                if username == uname.capitalize():
                    return (username, role, dead, runs,
                            gs_killed, sk_killed, or_killed, tr_killed,
                            tres_collected, highscore)
            return False

    def update_player_score(self, player):
        """
        This gets all lines from file, finds a player line position in file
        and rewrites the whole file with updated score of the players
        """

        monsters_killed = self.monster_kill_count()
        with open("players.txt", "r") as f:
            lines = f.readlines()
        count = 0
        pos = 0
        for row in lines:
            if row.startswith(player.name):
                (username, role, dead, runs,
                 gs_killed, sk_killed, or_killed, tr_killed,
                 tres_collected, highscore) = row.split(sep=",")
                pos = count
            count += 1

        new_r = int(runs) + 1
        new_g_kill = int(gs_killed) + monsters_killed["giant spider"]
        new_s_kill = int(sk_killed) + monsters_killed["skeleton"]
        new_o_kill = int(or_killed) + monsters_killed["orc"]
        new_t_kill = int(tr_killed) + monsters_killed["troll"]
        t = int(tres_collected) + len(self.looted_items)
        s = player.score+int(highscore)

        lines[pos] = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}\n".format(
                      player.name, player.hero_class, "0", new_r,
                      new_g_kill, new_s_kill, new_o_kill, new_t_kill,
                      t, s)
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
                if x[2] == "1":
                    scores.append("{:006d}{s}{:>20s}".format(int(x[-1]), x[0], s="  DEAD"))
                else:
                    scores.append("{:006d}{:>26s}".format(int(x[-1]), x[0]))
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
            uclass = self.view.handle_input()
            if uclass == "1":
                uname = "Ai knight"
                break
            elif uclass == "2":
                uname = "Ai wizard"
                break
            elif uclass == "3":
                uname = "Ai thief"
                break
            else:
                self.view.print_main_menu(View.choose_AI,
                                          View.err_choice,
                                          error=True)

        player_tuple = self.load_players_file(uname)
        self.print_load_stats(*player_tuple)
        return player_tuple[0], player_tuple[1]

    def generate_exit(self, dungeon_size, dungeon, start_room):
        """
        This will generate an exit
        It will generate a new exit if the
        location is the same as the player
        start_room
        """
        while True:
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
            player.profile = "brave"
            player.start_room = start_room
            player.destination = self.ai_find_exit(player, dungeon)
        player.current_room.monsters = []
        player.current_room.treasures = []
        player.current_room.is_dark = False

        self.game_loop(player, dungeon)  # Should we run this here?

    def ai_find_exit(self, player, dungeon):
        """
        Takes player + dungeon. If player is in a corner (which happens during start),
        game will tell player to find the opposite corner.
        If the player knows where the exit is (is_dark False + has_exit is True),
        the destination instead becomes the exit.
        """
        if player.start_room.position == (0, 0):
            player.destination = dungeon.get_room(dungeon.size-1, dungeon.size-1)
        elif player.start_room.position == (dungeon.size-1, 0):
            player.destination = dungeon.get_room(0, dungeon.size-1)
        elif player.start_room.position == (0, dungeon.size-1):
            player.destination = dungeon.get_room(dungeon.size-1, 0)
        elif player.start_room.position == (dungeon.size-1, dungeon.size-1):
            player.destination = dungeon.get_room(0, 0)
        for row in dungeon:
            for room in row:
                if room.is_dark is False:
                    if room.has_exit is True:
                        player.destination = room
        return player.destination

    def ai_simple_move(self, player):
        """
        Knowing player.destination, it moves horizontally or vertically towards destination tile.
        Bug: If AI is fleeing to default destination (opposite corner), it is stuck there if it does not know
        where the exit tile is (should probably try to snake towards starting corner in that case).
        Returns direction (w, e, s, n)
        """
        time.sleep(0.5)
        room_x = player.current_room.position[0]
        room_y = player.current_room.position[1]
        dest_x = player.destination.position[0]
        dest_y = player.destination.position[1]
        if room_x > dest_x:
            direction = "w"
        elif room_x < dest_x:
            direction = "e"
        elif room_y > dest_y:
            direction = "n"
        elif room_y < dest_y:
            direction = "s"
        elif player.current_room.position == player.destination.position:
            print("found destination")
            time.sleep(0.2)
            direction = "find new target"
        else:
            print("ended in Else for simple move - bug")
            direction = 0
            quit()
        return direction

    def ai_snake_move(self, player, dungeon):
        '''
        Uses ai_find_exit to calc. exit square, then moves in a serpentine direction by checking if it's position
        alignes with the start room or exit room (if it does, go vertically, otherwise, horizontally)
        Due to the shape of some maps (4 or 8) it cannot find all rooms by snaking.
        However, this is technically within acceptable parameters for AI requirements.
        Function returns direction
        '''
        start_x = player.start_room.position[0]  # no need to check start_y since it moves horizontally primarily
        room_x = player.current_room.position[0]
        room_y = player.current_room.position[1]
        dest_x = player.destination.position[0]
        dest_y = player.destination.position[1]
        time.sleep(0.5)

        # start in NW
        if player.start_room == dungeon.get_room(0, 0):
            print(player.destination.position)
            if room_y == dest_y:
                # AI has reached final row
                if dungeon.size == 5:
                    if dungeon.get_room(room_x+1, dungeon.size - 1).is_dark is True:
                        direction = "e"
                    else:
                        return "find new target"
                else:
                    if dungeon.get_room(room_x-1, dungeon.size-1).is_dark is True:
                        direction = "w"
                    else:
                        return "find new target"
            if room_y % 2 == 0:
                if room_x == dest_x:
                    direction = "s"
                else:
                    direction = "e"
            elif room_y % 2 != 0:
                if room_x == start_x:
                    direction = "s"
                else:
                    direction = "w"

        # start in NE
        elif player.start_room == dungeon.get_room(dungeon.size-1, 0):
            print(player.destination.position)
            if room_y == dest_y:
                # AI has reached final row
                if dungeon.size == 5:
                    try:
                        if dungeon.get_room(room_x-1, dungeon.size - 1).is_dark is True:
                            direction = "w"
                    except IndexError:
                        return "find new target"
                else:
                    try:
                        if dungeon.get_room(room_x+1, dungeon.size-1).is_dark is True:
                            direction = "e"
                    except IndexError:
                        return "find new target"
            if room_y % 2 == 0:
                if room_x == dest_x:
                    direction = "s"
                else:
                    direction = "w"
            if room_y % 2 != 0:
                if room_x == start_x:
                    direction = "s"
                else:
                    direction = "e"

        # start in SW
        elif player.start_room == dungeon.get_room(0, dungeon.size-1):
            print(player.destination.position)
            if room_y == dest_y:
                # AI has reached final row
                if dungeon.size == 5:
                    if dungeon.get_room(room_x+1, 0).is_dark is True:
                        direction = "e"

                    else:
                        return "find new target"
                else:
                    if dungeon.get_room(room_x-1, 0).is_dark is True:
                        direction = "w"

                    else:
                        return "find new target"
            if dungeon.size % 2 != 0:
                if room_y % 2 == 0:
                    if room_x == dest_x:
                        direction = "n"
                    else:
                        direction = "e"
                elif room_y % 2 != 0:
                    if room_x == start_x:
                        direction = "n"
                    else:
                        direction = "w"
            else:
                if room_y % 2 != 0:
                    if room_x == dest_x:
                        direction = "n"
                    else:
                        direction = "e"
                elif room_y % 2 == 0:
                    if room_x == start_x:
                        direction = "n"
                    else:
                        direction = "w"

        # start in SE
        elif player.start_room == dungeon.get_room(dungeon.size-1, dungeon.size-1):
            if room_y == dest_y:
                print(player.destination.position)
                # AI has reached final row
                if dungeon.size == 5:
                    try:
                        if dungeon.get_room(room_x-1, 0).is_dark is True:
                            direction = "w"
                    except IndexError:
                        return "find new target"
                else:
                    try:
                        if dungeon.get_room(room_x+1, 0).is_dark is True:
                            direction = "e"
                    except IndexError:
                        return "find new target"
            if dungeon.size % 2 != 0:
                if room_y % 2 == 0:
                    if room_x == dest_x:
                        direction = "n"
                    else:
                        direction = "w"
                elif room_y % 2 != 0:
                    if room_x == start_x:
                        direction = "n"
                    else:
                        direction = "e"
            else:
                if room_y % 2 != 0:
                    if room_x == dest_x:
                        direction = "n"
                    else:
                        direction = "w"
                elif room_y % 2 == 0:
                    if room_x == start_x:
                        direction = "n"
                    else:
                        direction = "e"

        elif player.current_room.position == player.destination.position:
            print("found destination")
            temp = player.start_room
            player.start_room = player.destination
            player.destination = temp
            direction = "idk"

        else:
            print("bug in snake move")
            direction = 0
            quit()

        return direction

    def set_ai_profile(self, player, dungeon):
        """
        runs in game_loop, every time player is prompted to move.
        returns profile (player.profile)
        """
        if player.score == 0:
            profile = "brave"
        elif player.hp == 1 and self.ai_find_exit(player, dungeon).has_exit:
            profile = "coward"
        else:  # IF you have 2+ hp AND you have coin:
            count = 0
            for row in dungeon:
                for room in row:
                    if room.is_dark is True:
                        count += 1
            if count == 0:  # If all rooms are explored, go straight to exit
                profile = "coward"
            else:
                # Defaulting to brave
                profile = "brave"
        return profile

    def game_loop(self, player, dungeon):
        """
        Main game loop, takes in player and dungeon and let the player
        play in the dungeon! :)
        """

        while True:
            self.view.print_game(player, dungeon, View.direction_option)

            # ASK PLAYER DIRECTION
            if player.ai is True:
                player.profile = self.set_ai_profile(player, dungeon)
                print("My profile is:", player.profile)
                if player.profile == "coward":
                    self.ai_find_exit(player, dungeon)
                    direction = self.ai_simple_move(player)
                    print("Fleeing:", direction, "towards", player.destination.position)
                    time.sleep(1)
                else:
                    count = 0
                    for row in dungeon:
                        for room in row:
                            if room.is_dark is True:
                                count += 1
                    if count == 0:
                        self.ai_find_exit(player, dungeon)
                        direction = self.ai_simple_move(player)
                        print("All rooms are bright. Going", direction, "towards", player.destination.position)
                        time.sleep(2)
                    else:
                        direction = self.ai_snake_move(player, dungeon)
                        print("snekking:", direction, "towards", player.destination.position)
                        time.sleep(0.3)
                    if direction == "find new target":
                        self.ai_find_exit(player, dungeon)
                        direction = self.ai_snake_move(player, dungeon)
                        time.sleep(0.2)
            else:
                direction = self.view.handle_input()

            new_room = self.move_player(player, direction, dungeon)

            if new_room is False:
                self.view.print_game(player,
                                     dungeon,
                                     View.direction_option,
                                     View.err_choice,
                                     error=True)
                if player.ai is False:
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
                    if player.ai is True:
                        if player.profile == "coward":
                            usrinp = "1"
                        else:
                            usrinp = "2"
                    else:
                        usrinp = self.view.handle_input()
                    if usrinp == "1":
                        self.statistics(player)
                        if player.ai is False:
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
                if player.ai is False:
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
        monsters_killed = self.monster_kill_count()

        # RESULTS [1] KILLED
        # RESULTS [2] TREASURES
        # RESULT [3] TOTAL SCORE
        if not self.is_player_dead(player.name):
            self.update_player_score(player)
            results[2] += str(monsters_killed["giant spider"])
            results[3] += str(monsters_killed["skeleton"])
            results[4] += str(monsters_killed["orc"])
            results[5] += str(monsters_killed["troll"])
            results[7] += str(len(self.looted_items))
            results[8] += str(player.score)
            results[10] = View.exit_score[0]
            results[11] = View.enter_go_back[2]

            self.view.print_main_menu(results)
        else:
            self.view.print_main_menu(View.you_died)
        usr_input = self.view.handle_input()
        self.main_menu()
    
    def print_load_stats(self, name, role, d, runs, spider, skeleton, orc, troll, t, hs):
        results = View.player_load_stats.copy()
        results[1] += runs
        results[4] += spider
        results[5] +=skeleton
        results[6] += orc 
        results[7] += troll
        results[9] += t
        results[10] += hs.strip('\n') 
        self.view.print_main_menu(results)
        self.view.handle_input()

    def monster_kill_count(self):
        """
        Takes no input
        Counts all killed monster types
        and returns dict of killed monsters
        """
        killed_gs = 0
        killed_sk = 0
        killed_or = 0
        killed_tr = 0

        for monster in self.killed_monsters:
            if monster.unit_type == "giant spider":
                killed_gs += 1
            if monster.unit_type == "skeleton":
                killed_sk += 1
            if monster.unit_type == "orc":
                killed_or += 1
            if monster.unit_type == "troll":
                killed_tr += 1

        return {"giant spider": killed_gs, "skeleton": killed_sk,
                "orc": killed_or, "troll": killed_tr}

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
            if player.ai is False:
                time.sleep(3)

        return looted

    def combat(self, player, dungeon):
        """
        Takes in player and dungeon
        Runs combats and returns true or false
        SUGGESTION: RETURNS WON, ESCAPED OR LOST
        """
        if player.ai is True:
            player.profile = self.set_ai_profile(player, dungeon)
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
                    if player.ai is False:
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
                    if player.ai is False:
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
                            if player.ai is False:
                                time.sleep(2)
                            break
                        elif choice == "2":
                            escape = player.escape_combat()
                            if escape:
                                player.current_room = player.old_room
                                self.view.print_game(player,
                                                     dungeon,
                                                     View.player_escaped)
                                if player.ai is False:
                                    time.sleep(2)
                                initiative_list.clear()
                                return False
                            else:
                                self.view.print_game(player,
                                                     dungeon,
                                                     View.player_failed_escape)
                                if player.ai is False:
                                    time.sleep(3)
                                break
                else:
                    result = self.attack_function(actor, player)
                    self.view.print_game(player,
                                         dungeon,
                                         *result,
                                         show_result=True)
                    if player.ai is False:
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
                        if defender.hp == 1:
                            defender.hp -= 1
                            result = [View.player_crit[0], defender.unit_type]
                            return result
                        else:
                            defender.hp -= 2
                            result = [View.player_crit[0], defender.unit_type]
                            return result
                    else:
                        defender.hp -= 1
                        return View.player_hit, defender.unit_type
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
