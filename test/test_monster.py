import unittest

from dungeonrun.monster import Monster
from dungeonrun.dungeon import Map


class testMap(unittest.TestCase):

    def setUp(self):
        self.dungeon = Map(4)

        self.monster_list = [m for m in Monster.available_monsters]

        self.spider = Monster("giant spider", self.dungeon.get_room(1, 2))
        self.skeleton = Monster("skeleton", self.dungeon.get_room(0, 3))
        self.orc = Monster("orc", self.dungeon.get_room(1, 0))
        self.troll = Monster("troll", self.dungeon.get_room(2, 2))

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
