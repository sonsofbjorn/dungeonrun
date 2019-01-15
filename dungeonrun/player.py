import random
DEFAULT_HP = 100


class Player:
    def __init__(self, name, hero_class, start_room, score=0, hp=DEFAULT_HP):
        self.name = name.capitalize()
        self.hp = hp
        self.hero_class = hero_class
        self.current_room = start_room
        self.score = score

        if hero_class.lower() == "knight":
            self.initiative = 5
            self.hp = 9
            self.attack = 6
            self.dexterity = 4

        elif hero_class.lower() == "wizard":
            self.initiative = 6
            self.hp = 4
            self.attack = 9
            self.dexterity = 5

        elif hero_class.lower() == "thief":
            self.initiative = 7
            self.hp = 5
            self.attack = 5
            self.dexterity = 7

        else:
            raise Exception("No such class")

    def generate_attack(self):
        attack_value = 0
        for x in range(0, self.attack):
            attack_value += random.randrange(0, self.attack)
        return attack_value

    def generate_dodge(self):
        dodge_value = 0
        for x in range(0, self.dexterity):
            dodge_value += random.randrange(0, self.dexterity)
        return dodge_value

    @property
    def show_location(self):
        return self.current_room.position

    def move_character(self, direction, dungeon_map):
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
            raise Exception("How did you enter else?")
        new_room.dark = False
        self.current_room = new_room
        return new_room

    def escape_combat(self):
        escape_chance = self.dexterity*10
        escape = random.randrange(0, 100)
        if escape >= escape_chance:
            escape = True
        else:
            escape = False
        return escape
