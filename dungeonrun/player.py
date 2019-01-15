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
            self.hp = 2
            self.attack = 9
            self.dexterity = 5

        elif hero_class.lower() == "thief":
            self.initiative = 7
            self.hp = 5
            self.attack = 5
            self.dexterity = 7

        else:
            raise Exception("No such class")

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

    def attack_function(self, monster):
        attacker_roll = self.roll_dice("attack")
        monster_roll = monster.roll_dice("dexterity")
        if attacker_roll > monster_roll:
            if self.hero_class == "thief":
                critical_hit = random.randrange(0, 100)
                if critical_hit >= 75:
                    monster.hp -= 2
                else:
                    print("You attack the", monster.name, "and hit!")
                    monster.hp -= 1
            else:
                print("You attack the", monster.name, "and hit!")
                monster.hp -= 1
                if monster.hp > 0:
                    print(monster.name, "current hp is:", monster.hp)
        else:
            print("You attack", monster.name + ", but you miss!")

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
            return False
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
