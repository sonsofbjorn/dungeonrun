import unittest

from dungeonrun import dungeon

class mapSizeTest(unittest.TestCase):

    def runTest(self):
        map = dungeon.Map(4)
        self.assertEqual(map.size, 4)
