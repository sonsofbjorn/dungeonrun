import random


class Monster:
    def __init__(self, name, position):
        self.name = name
        self.position = position

        if self.name.lower() == "giant spider":
            self.initiative =7
            self.hp = 1
            self.attack = 2
            self.dexterity = 3
            self.rarity = 20

        if self.name.lower() == "skeleton":
            self.initiative = 4
            self.hp = 2
            self.attack = 3
            self.dexterity = 3
            self.rarity = 15

        if self.name.lower() == "orc":
            self.initiative = 6
            self.hp = 3
            self.attack = 4
            self.dexterity = 4
            self.rarity = 10

        if self.name.lower() == "troll":
            self.initiative = 2
            self.hp = 4
            self.attack = 7
            self.dexterity = 2
            self.rarity = 5

    def generate_attack(self):
        attack_value = 0
        for x in range(0, self.attack):
            attack_value += random.randrange(0, self.attack)
        return attack_value
