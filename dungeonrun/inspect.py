from dungeon import * 
from player import * 

# Setup
size = 4
dungeon = Map(size)


import pprint
for row in dungeon:
    for room in row:
        print(f"Room 0x{id(room)}: ")
        pprint.pprint(room.__dict__)

#print("Monsters: ")
#print(dungeon.print_monsters())
#print(dungeon.print_treasures())
