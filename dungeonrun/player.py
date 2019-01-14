import random
DEFAULT_HP = 100


class Player:
    def __init__(self, name, hero_class, start_room, hp=DEFAULT_HP, score=0):
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

    @property
    def show_location(self):
        return self.current_room.position

    def move_character(self, room):
        self.current_room = room
