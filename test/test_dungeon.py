import unittest

from dungeonrun import dungeon


class mapSizeTest(unittest.TestCase):

    def setUp(self):
        self.dungeon = dungeon.Map(4)

    def testMapSize(self):
        self.assertEqual(self.dungeon.size, 4)

    def testRoomPosition(self):
        self.assertEqual(self.dungeon.room(0, 1).position, (0, 1))
