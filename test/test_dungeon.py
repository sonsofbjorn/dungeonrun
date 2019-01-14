import unittest

from dungeonrun import dungeon
from collections import Iterable


class testDungeon(unittest.TestCase):

    def setUp(self):
        self.dungeon = dungeon.Map(4)

    def testMapSize(self):
        self.assertEqual(self.dungeon.size, 4)

    def testRoomPosition(self):
        self.assertEqual(self.dungeon.get_room(0, 1).position, (0, 1))

    def testIterableMap(self):
        self.assertTrue(isinstance(self.dungeon, Iterable))

    def testRoomDoorsNW(self):
        self.assertFalse(self.dungeon.get_room(0, 0).doors["N"])
        self.assertFalse(self.dungeon.get_room(0, 0).doors["W"])

    def testRoomDoorsSE(self):
        self.assertFalse(self.dungeon.get_room(3, 2).doors["E"])
        self.assertTrue(self.dungeon.get_room(3, 2).doors["W"])
        self.assertTrue(self.dungeon.get_room(3, 2).doors["N"])
        self.assertTrue(self.dungeon.get_room(3, 2).doors["S"])




    def testRoomDoorsSE(self):
        self.assertTrue(self.dungeon.get_room(2, 2).doors["E"])
        self.assertTrue(self.dungeon.get_room(2, 2).doors["W"])
        self.assertTrue(self.dungeon.get_room(2, 2).doors["N"])
        self.assertTrue(self.dungeon.get_room(2, 2).doors["S"])


