import unittest

from dungeonrun import dungeon
from dungeonrun import player

class mapSizeTest(unittest.TestCase):

    def setUp(self):
        self.map = dungeon.Map(4)

    def testMapSize(self):
        self.assertEqual(self.map.size, 4)

    def testRoomPosition(self):
        self.assertEqual(self.map.matrix[0][1].position, (0 ,1))


