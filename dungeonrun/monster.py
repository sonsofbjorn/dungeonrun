import random


class Monster:
    available_monsters = {"giant spider": {
                                    "initiative": 7,
                                    "hp": 1,
                                    "attack": 2,
                                    "dexterity": 3,
                                    "rarity": 20},
                          "skeleton": {
                                    "initiative": 4,
                                    "hp": 2,
                                    "attack": 2,
                                    "dexterity": 3,
                                    "rarity": 15},
                          "orc": {
                                    "initiative": 6,
                                    "hp": 3,
                                    "attack": 4,
                                    "dexterity": 5,
                                    "rarity": 10},
                          "troll": {
                                    "initiative": 2,
                                    "hp": 4,
                                    "attack": 7,
                                    "dexterity": 2,
                                    "rarity": 5}}

    def __init__(self, unit_type, room):
        self.room = room


        self.unit_type = self.available_monsters[unit_type]

        self.__dict__ = self.unit_type

        def __iter__():
            for monsters in self.available_monsters:
                yield monsters

    def generate_attack(self):
        attack_value = 0
        for x in range(0, self.attack):
            attack_value += random.randrange(0, self.attack)
        return attack_value
