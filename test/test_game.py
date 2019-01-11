import dungeonrun
from dungeonrun import game

import unittest

class mapSizeTest(unittest.TestCase):

    def setup_map(self):
        map = Map(4)
        self.assertEqual(map.size(), 4)
