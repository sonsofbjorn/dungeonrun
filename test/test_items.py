import unittest

from game.dungeon import Map, Treasure

class testItems(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.dungeon = Map(4)

        self.change = Treasure("loose change", self.dungeon.get_room(1, 2))
        self.pouch = Treasure("money pouch", self.dungeon.get_room(0, 3))
        self.gold = Treasure("gold jewelry", self.dungeon.get_room(1, 0))
        self.gem = Treasure("gemstone", self.dungeon.get_room(2, 2))
        self.chest = Treasure("small treasurechest", self.dungeon.get_room(2, 2))

    def testChangeProperties(self):
        self.assertEqual(self.change.value, 2)
        self.assertEqual(self.change.rarity,40)

    def testPouchProperties(self):
        self.assertEqual(self.pouch.value, 6)
        self.assertEqual(self.pouch.rarity, 20)

    def testGoldProperties(self):
        self.assertEqual(self.gold.value, 10)
        self.assertEqual(self.gold.rarity, 15)

    def testGemProperties(self):
        self.assertEqual(self.gem.value, 14)
        self.assertEqual(self.gem.rarity, 10)

    def testChestProperties(self):
        self.assertEqual(self.chest.value, 20)
        self.assertEqual(self.chest.rarity, 5)

    def testCollectItems(self):
        loot = []
        max_loot = 4**2 * ( 20 + 14 + 10 + 6 + 2 )
        for row in self.dungeon:
            for room in row:
                loot += room.treasures
        self.assertLessEqual(sum(map(lambda l: l.value, loot)), max_loot)
