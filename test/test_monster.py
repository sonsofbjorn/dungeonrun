import unittest

from dungeonrun import monster

class mapSizeTest(unittest.TestCase):

    def setUp(self):
        self.spider = monster.Monster("giant spider", (1, 2))
        self.skeleton = monster.Monster("skeleton",   (1, 2))
        self.orc = monster.Monster("orc",             (1, 2))
        self.troll = monster.Monster("troll",         (1, 2))

    def testSpiderProperties(self):
        self.assertEqual(self.spider.initiative, 7)
        self.assertEqual(self.spider.hp,         1)
        self.assertEqual(self.spider.attack,     2)
        self.assertEqual(self.spider.dexterity,  3)
        self.assertEqual(self.spider.rarity,     20)

    def testSkeletonProperties(self):
        self.assertEqual(self.skeleton.initiative, 4)
        self.assertEqual(self.skeleton.hp,         2)
        self.assertEqual(self.skeleton.attack,     3)
        self.assertEqual(self.skeleton.dexterity,  3)
        self.assertEqual(self.skeleton.rarity,     15)

    def testOrcProperties(self):
        self.assertEqual(self.orc.initiative, 6)
        self.assertEqual(self.orc.hp,         3)
        self.assertEqual(self.orc.attack,     4)
        self.assertEqual(self.orc.dexterity,  4)
        self.assertEqual(self.orc.rarity,     10)

    def testTrollProperties(self):
        self.assertEqual(self.troll.initiative, 2)
        self.assertEqual(self.troll.hp,         4)
        self.assertEqual(self.troll.attack,     7)
        self.assertEqual(self.troll.dexterity,  2)
        self.assertEqual(self.troll.rarity,     5)
