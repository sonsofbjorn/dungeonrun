import unittest

from dungeonrun import dungeon

class mapSizeTest(unittest.TestCase):

    def setUp(self):
        self.map = dungeon.Map(4)

    def runTest(self):
        self.assertEqual(self.map.size, 4)
