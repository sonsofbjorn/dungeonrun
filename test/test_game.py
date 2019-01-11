import unittest

import dungeonrun
from dungeonrun import game


class mapSizeTest(unittest.TestCase):

    def runTest(self):
        map = dungeonrun.game.Map(4)
        self.assertEqual(map.size, 4)



