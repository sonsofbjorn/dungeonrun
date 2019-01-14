import unittest
import os
from dungeonrun import menu


class testMenu(unittest.TestCase):
    def setUp(self):
        menu.saveNewPlayer("bob", "knight", 100, 200)

    def testPlayerExists(self):
        self.assertTrue(menu.playerExists("bob"))
        self.assertFalse(menu.playerExists("oaiwjfp8q34hrå8awhripuaw3hrå8a3r9awhrpaiuw3hriuwrhpihriwrh"))

    def testLoadPlayer(self):
        self.assertTrue(menu.loadPlayer("bob"))

    def tearDown(self):
        os.remove("players.txt")
