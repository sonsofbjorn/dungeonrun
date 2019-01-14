import unittest

from dungeonrun import view
from dungeonrun import player
from dungeonrun import dungeon

class testView(unittest.TestCase):

    def setUp(self):
        self.m = dungeon.Map(4)
        self.p = player.Player("bob", "knight", self.m.get_room(0, 1))
        self.v = view.View(self.m, self.p)


    def testMap(self):
        self.v.draw_map()

    def testMovePlayer(self):
        self.p.move_character(self.m.get_room(0, 2))

