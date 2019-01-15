import random


class Monster:
    def __init__(self, name, position):
        self.name = name
        self.position = position

        if self.name.lower() == "giant spider":
            self.initiative = 7
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
            print(player.name, "is hit by", self.name + "!")
            player.hp -= 1
            print("you have", player.hp, "hp remaining!")
        else:
            print(self.name, "attacks", player.name + ", but misses!")

