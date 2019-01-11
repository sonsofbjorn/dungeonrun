DEFAULT_HP=100

class Player:
    def __init__(self, name, hero_class, start_pos, hp=DEFAULT_HP):
        self.name = name.capitalize()
        self.hp = hp
        self.hero_class = hero_class
        self.position = start_pos

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

