import random
DEFAULT_HP = 10


class Player:
    def __init__(self, name, hero_class, start_room, score=0, hp=DEFAULT_HP):
        self.name = name.capitalize()
        self.hp = hp
        self.hero_class = hero_class
        self.current_room = start_room
        self.score = score
        self.old_room = start_room

        if hero_class.lower() == "knight":
            self.initiative = 5
            self.hp = 9
            self.attack = 6
            self.dexterity = 4
            self.special_ability = "block"

        elif hero_class.lower() == "wizard":
            self.initiative = 6
            self.hp = 4
            self.attack = 9
            self.dexterity = 5
            self.special_ability = "light"

        elif hero_class.lower() == "thief":
            self.initiative = 7
            self.hp = 5
            self.attack = 5
            self.dexterity = 7
            self.special_ability = "crit"

        else:
            raise Exception("No such class")

        self.max_hp = self.hp

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

    def attack_function(self, enemy):
        attacker_roll = self.roll_dice("attack")
        monster_roll = enemy.roll_dice("dexterity")
        if attacker_roll > monster_roll:
            if self.special_ability == "crit":
                critical_hit = random.randrange(0, 100)
                if critical_hit >= 75:
                    print("OH YEAH, IT'S A CRITICAL HIT!")
                    enemy.hp -= 2
                else:
                    print("You attack the", enemy.unit_type, "and hit!")
                    enemy.hp -= 1
            else:
                print("You attack the", enemy.unit_type, "and hit!")
                enemy.hp -= 1
                if enemy.hp > 0:
                    print(enemy.unit_type, "current hp is:", enemy.hp)
        else:
            print("You attack", enemy.unit_type + ", but you miss!")

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
        self.old_room = self.current_room
        self.current_room = new_room
        return new_room

    def escape_combat(self):
        if self.special_ability == "light":
            escape_chance = 20  # 20-100: you gucci
        else:
            escape_chance = self.dexterity*10
        escape = random.randrange(0, 100)
        if escape >= escape_chance:
            escape = True
        else:
            escape = False
        return escape
