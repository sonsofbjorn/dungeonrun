import unittest
from game import controller
from game.view import View


class testHighscore(unittest.TestCase):

    def setUp(self):
        self.cont = controller.Controller()

    def testTopHighscore(self):
        self.cont.save_player('testarmassahär', 'knight', '0', '99999')
        user = "{:006d}{:>20s}".format(99999, 'Testarmassahär')
        topscores = self.cont.get_top_highscores()

        self.assertEqual(topscores[1], user)