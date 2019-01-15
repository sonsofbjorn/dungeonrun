import random


class Monster:

    available_monsters = {"giant spider": {
                              "unit_type": "giant spider",
                              "initiative": 7,
                              "hp": 1,
                              "attack": 2,
                              "dexterity": 3,
                              "rarity": 20},
                          "skeleton": {
                              "unit_type": "skeleton",
                              "initiative": 4,
                              "hp": 2,
                              "attack": 3,
                              "dexterity": 3,
                              "rarity": 15},
                          "orc": {
                              "unit_type": "orc",
                              "initiative": 6,
                              "hp": 3,
                              "attack": 4,
                              "dexterity": 4,
                              "rarity": 10},
                          "troll": {
                              "unit_type": "troll",
                              "initiative": 2,
                              "hp": 4,
                              "attack": 7,
                              "dexterity": 2,
                              "rarity": 5}}

    def __init__(self, unit_type, room):
        self.hp = self.available_monsters[unit_type["hp"]]

        self.room = room

        self.unit_type = self.available_monsters[unit_type]

        self.__dict__ = self.unit_type

        def __iter__():
            for monsters in self.available_monsters:
                yield monsters

    def roll_dice(self, dice_type):
        if dice_type == "attack":
            dice_type = self.attack
        elif dice_type == "dexterity":
            dice_type = self.dexterity
        elif dice_type == "initiative":
            dice_type = self.initiative
        value = 0
        for x in range(0, dice_type):
            value += random.randrange(0, dice_type)
        return value

    def attack_function(self, player):
        attacker_roll = self.roll_dice("attack")
        player_roll = player.roll_dice("dexterity")
        if attacker_roll > player_roll:
            if player.hero_class == "knight":
                # Another IF needed to see if player blocks attack
                print("something something knight shield")
            print(player.name, "is hit by", str(self.unit_type) + "!")
            player.hp -= 1
            print("you have", player.hp, "hp remaining!")
        else:
            print(self.unit_type, "attacks", player.name + ", but misses!")
