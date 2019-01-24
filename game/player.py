import random

class Player:
    def __init__(self, name, hero_class, start_room, score=0):
        """
        Makes a player object. Takes name, class, start room and score
        Name is a string, class is one of the classes below and start room
        is a room object.
        """
        self.name = name.capitalize()
        self.hero_class = hero_class
        self.current_room = start_room
        self.score = score
        self.old_room = start_room
        self.ai = False

        if hero_class.lower() == "knight":
            self.initiative = 5
            self.hp = 9
            self.attack = 6
            self.dexterity = 4
            self.special_ability = "block"

        elif hero_class.lower() == "wizard":
            self.initiative = 6
            self.hp = 4
            self.attack = 9
            self.dexterity = 5
            self.special_ability = "light"

        elif hero_class.lower() == "thief":
            self.initiative = 7
            self.hp = 5
            self.attack = 5
            self.dexterity = 7
            self.special_ability = "crit"

        else:
            raise Exception("No such class")

        self.max_hp = self.hp

    @property
    def show_location(self):
        """
        Return x, y tuple
        """
        return self.current_room.position

    def move_character(self, direction, dungeon_map):
        """
        Takes a direction strong (WNES) and returns a room object
        """
        x = self.current_room.position[0]
        y = self.current_room.position[1]

        direction = direction.upper()[:1]

        while True:
            if self.current_room.doors.get(direction) is False:
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
        self.old_room = self.current_room
        self.current_room = new_room
        return new_room

    def escape_combat(self):
        """Flee function. Returns whether you have fled successfully or not"""
        if self.special_ability == "light":
            escape_chance = 80  # 20-100: you gucci
        else:
            escape_chance = self.dexterity*10
        escape = random.randrange(0, 100)
        if escape <= escape_chance:
            return True
        else:
            return False
