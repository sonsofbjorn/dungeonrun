import unittest

from dungeonrun.monster import Monster
from dungeonrun.dungeon import Map


class testMap(unittest.TestCase):

    def setUp(self):
        self.dungeon = Map(4)
        self.spider = Monster("giant spider", self.dungeon.get_room(1, 2))

    def testSpiderProperties(self):
        self.assertEqual(self.spider.initiative, 7)
        self.assertEqual(self.spider.hp,         1)
        self.assertEqual(self.spider.attack,     2)
        self.assertEqual(self.spider.dexterity,  3)
        self.assertEqual(self.spider.rarity,     20)
