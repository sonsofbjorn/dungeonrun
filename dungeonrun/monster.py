import random


class Monster:
    def __init__(self, unit_type, room):
        self.room = room

        self.available_monsters = {"giant spider": {
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
                                       "initiative": 4,
                                       "hp": 2,
                                       "attack": 2,
                                       "dexterity": 3,
                                       "rarity": 15},
                                   "troll": {
                                       "initiative": 4,
                                       "hp": 2,
                                       "attack": 2,
                                       "dexterity": 3,
                                       "rarity": 15}}

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
