import unittest

from dungeonrun.player import Player
from dungeonrun.dungeon import Map


class testPlayer(unittest.TestCase):
    def setUp(self):
        start_pos = (1, 2)
        self.knight = Player("Knightsebbe", "knight",   start_pos)
        self.wizard = Player("wizSeb",      "wizard",   start_pos)
        self.thief = Player("thiefSeb",    "thief",    start_pos)

        self.dungeon = Map(4)

        self.char = Player("Bob", "knight", self.dungeon.get_room(1, 1))
        self.char2 = Player("Bob", "knight", self.dungeon.get_room(0, 1))

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

    def testMovePlayerNorth(self):
        new_room = self.char.move_character('N', self.dungeon)
        self.assertEqual(new_room, self.dungeon.get_room(1, 0))

    def testMovePlayerSouth(self):
        new_room = self.char.move_character('S', self.dungeon)
        self.assertEqual(new_room, self.dungeon.get_room(1, 2))

    def testMovePlayerEast(self):
        new_room = self.char.move_character('E', self.dungeon)
        self.assertEqual(new_room, self.dungeon.get_room(2, 1))

    def testMovePlayerWest(self):
        new_room = self.char.move_character('W', self.dungeon)
        print(new_room.position)
        self.assertEqual(new_room, self.dungeon.get_room(1, 2))

    def testMovePlayerOtOfBounds(self):
        new_room = self.char.move_character('N', self.dungeon)
        new_room = self.char.move_character('N', self.dungeon)
        self.assertFalse(new_room)
