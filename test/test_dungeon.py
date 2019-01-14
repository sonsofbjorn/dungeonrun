import unittest
from collections import Iterable

from dungeonrun import dungeon


class mapSizeTest(unittest.TestCase):

    def setUp(self):
        self.dungeon = dungeon.Map(4)

    def testMapSize(self):
        self.assertEqual(self.dungeon.size, 4)

    def testRoomPosition(self):
        self.assertEqual(self.dungeon.get_room(0, 1).position, (0, 1))

    def testIterableMap(self):
        self.assertTrue(isinstance(dungeon, Iterable))
