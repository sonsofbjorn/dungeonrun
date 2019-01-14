import unittest
from dungeonrun import menu


class testMenu(unittest.TestCase):
    def setUp(self):
        self.m = menu.Menu()
        menu.saveNewPlayer("bob", "knight", 100, 200)

    def testPlayerExists(self):
        self.assertTrue(menu.playerExists("bob"))
        self.assertFalse(menu.playerExists("oaiwjfp8q34hrå8awhripuaw3hrå8a3r9awhrpaiuw3hriuwrhpihriwrh"))

    def testLoadPlayer(self):
        self.assertTrue(menu.loadPlayer("bob"))

    def tearDown(self):
        with open("..//players.txt", "w") as f:
            line = f.readlines()
            line = line[:-1]
            #f.writelines(line)
