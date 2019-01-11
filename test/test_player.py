import unittest

from dungeonrun import player

class playerTest(unittest.TestCase):
    def setUp(self):
        start_pos = (1,2)
        self.knight = player.Player("Knightsebbe",     "knight",   start_pos)
        self.wizard = player.Player("wizSeb",    "wizard",   start_pos)
        self.thief = player.Player("thiefSeb",   "thief",    start_pos)

        self.dungeon = dungeon.Map(4)

        self.move_character = player.Player("Bob", "knight",
                                            dungeon.matrix[0][0])

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

    def testMovement(self):




dungeon = dungeon.Map(4)

dude = player.Player("Bob", "knight", dungeon.matrix[0][0])

dude.show_location()

newRoom = dungeon.enterDoor(dude.position, "north")

dude.move_character(newRoom)
