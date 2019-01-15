import math
class Room:
    def __init__(self, x,y, isDark=True,hasExit=False):
        self.position = (x,y)
        self.isDark = isDark
        self.hasExit = hasExit

size = 4
scale = 6
matrix = tuple(tuple(Room(x, y) for x in range(size)) for y in range(size))
matrix[0][0].hasExit = True
matrix[0][0].isDark = False
matrix[0][1].isDark = False
matrix[1][1].isDark = False

print("."+("-"*48)+".")
print("|"+(" "*48)+"|")
output = []
outrow = ""
for row in matrix:
    for n in range(scale//2):
        for room in row:
            if (room.isDark): out = "▓"*scale
            else: out = "░"*scale
            if (room.hasExit and n == 1):
                out = "░░[]░░"
            outrow += out
            out = ""
        output.append(outrow)
        outrow = ""
for row in output:
    print("|"+row.center(48)+"|")

print("|"+(" "*48)+"|")
print("*"+("-"*48)+"*")
