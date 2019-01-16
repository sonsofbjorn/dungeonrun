import unittest

from dungeonrun import view
from dungeonrun import player
from dungeonrun.dungeon import Map

class testView(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.m = Map(8)
        self.p = player.Player("SebastianDenAndreo", "knight", self.m.get_room(0, 1))
        self.v = view.View(self.m, self.p)
        self.m.get_room(2, 2).hasExit = True


#    def testMap(self):
 #       self.v.draw_map()
  #      print("\n")
    '''
    def testMovePlayer(self):
        print("\n")
        self.p.current_room.dark = False
        self.p.move_character(self.m.enter_door(self.p.current_room, "E"))
        self.p.move_character(self.m.enter_door(self.p.current_room, "E"))
        self.p.move_character(self.m.enter_door(self.p.current_room, "S"))
        self.p.move_character(self.m.enter_door(self.p.current_room, "E"))
        self.p.move_character(self.m.enter_door(self.p.current_room, "E"))
        self.p.move_character(self.m.enter_door(self.p.current_room, "N"))
        self.p.move_character(self.m.enter_door(self.p.current_room, "N"))
        self.v.draw_map()
        '''

    def testPrintIt(self):
        print("\n")
        self.v.print_start_menu(self.v.test_list())

    def testPrintMap(self):
        print("\n")
        self.v.print_game(self.v.draw_map2())


