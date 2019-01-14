import unittest

from dungeonrun import player
from dungeonrun import dungeon


class testPlayer(unittest.TestCase):
    def setUp(self):
        start_pos = (1, 2)
        self.knight = player.Player("Knightsebbe", "knight",   start_pos)
        self.wizard = player.Player("wizSeb",      "wizard",   start_pos)
        self.thief = player.Player("thiefSeb",    "thief",    start_pos)

        self.dungeon = dungeon.Map(4)

        self.char = player.Player("Bob", "knight", self.dungeon.get_room(1, 1))
        self.char2 = player.Player("Bob", "knight", self.dungeon.get_room(0, 1))

    def testKnightProperties(self):
        self.assertEqual(self.knight.initiative, 5)
        self.assertEqual(self.knight.hp,         9)
        self.assertEqual(self.knight.attack,     6)
        self.assertEqual(self.knight.dexterity,  4)

    def testWizardProperties(self):
        self.assertEqual(self.wizard.initiative, 6)
        self.assertEqual(self.wizard.hp,         4)
        self.assertEqual(self.wizard.attack,     9)
        self.assertEqual(self.wizard.dexterity,  5)

    def testThiefProperties(self):
        self.assertEqual(self.thief.initiative, 7)
        self.assertEqual(self.thief.hp,         5)
        self.assertEqual(self.thief.attack,     5)
        self.assertEqual(self.thief.dexterity,  7)

    def testPosition(self):
        self.assertEqual(self.char.show_location, (1, 1))

    def testPosition2(self):
        self.assertEqual(self.char2.show_location, (0, 1))

    def testMovementNorth(self):
        newRoom = self.dungeon.enter_door(self.char.current_room, "north")
        self.char.move_character(newRoom)
        self.assertEqual(self.char.show_location, (1, 0))

    def testMovementEast(self):
        newRoom = self.dungeon.enter_door(self.char.current_room, "east")
        self.char.move_character(newRoom)
        self.assertEqual(self.char.show_location, (2, 1))

    def testMovementSouth(self):
        newRoom = self.dungeon.enter_door(self.char.current_room, "south")
        self.char.move_character(newRoom)
        self.assertEqual(self.char.show_location, (1, 2))

    def testMovementWest(self):
        newRoom = self.dungeon.enter_door(self.char.current_room, "west")
        self.char.move_character(newRoom)
        self.assertEqual(self.char.show_location, (0, 1))
