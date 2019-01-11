

class Monster:
    def __init__(self, name, initiative, hp, attack, dexterity, rarity, position):
        self.name = name
        self.initiative = initiative
        self.hp = hp
        self.attack = attack
        self.dexterity = dexterity
        self.rarity = rarity
        self.position = position

    def create_skeleton(self):  # Spawn at X & Y 1
        self.name = "Skeletor"
        self.initiative = 4
        self.hp = 2
        self.attack = 3
        self.dexterity = 3
        self.rarity = 15
        self.position = [1, 2]
