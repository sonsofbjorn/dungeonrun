import unittest

import dungeonrun
from dungeonrun import dungeon


class mapSizeTest(unittest.TestCase):

    def runTest(self):
        map = dungeonrun.dungeon.Map(4)
        self.assertEqual(map.size, 4)



