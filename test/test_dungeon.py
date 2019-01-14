import unittest

from dungeonrun import dungeon
from collections import Iterable


class testDungeon(unittest.TestCase):

    def setUp(self):
        self.dungeon = dungeon.Map(4)
        self.monsterlist = self.dungeon.generate_monsters()

    def testMapSize(self):
        self.assertEqual(self.dungeon.size, 4)

    def testRoomPosition(self):
        self.assertEqual(self.dungeon.get_room(0, 1).position, (0, 1))

    def testIterableMap(self):
        self.assertTrue(isinstance(self.dungeon, Iterable))

    def testMonsterList(self):
        print("pringint monster list:")

    def testRoomDoorsNW(self):
        self.assertFalse(self.dungeon.corner["NW"].doors["N"])
        self.assertFalse(self.dungeon.corner["NW"].doors["W"])

    def testRoomDoorsNE(self):
        self.assertFalse(self.dungeon.corner["NE"].doors["N"])
        self.assertFalse(self.dungeon.corner["NE"].doors["E"])

    def testRoomDoorsSE(self):
        self.assertFalse(self.dungeon.corner["SE"].doors["S"])
        self.assertFalse(self.dungeon.corner["SE"].doors["E"])

    def testRoomDoorsSW(self):
        self.assertFalse(self.dungeon.corner["SW"].doors["S"])
        self.assertFalse(self.dungeon.corner["SW"].doors["W"])

    def testRoomN(self):
        self.assertFalse(self.dungeon.get_room(1, 0).doors["N"])

    def testRoomE(self):
        self.assertFalse(
            self.dungeon.get_room(self.dungeon.size-1, 1).doors["E"])

    def testRoomS(self):
        self.assertFalse(
            self.dungeon.get_room(1, self.dungeon.size-1).doors["S"])

    def testRoomW(self):
        self.assertFalse(self.dungeon.get_room(0, 1).doors["W"])
