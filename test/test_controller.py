import unittest
from dungeonrun.controller import Controller

class TestController(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.contrlr = Controller()

    def testMainMenu(self):
        self.contrlr.main_menu()
