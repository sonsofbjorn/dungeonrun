from dungeon import Map


def main():
    dungeon = Map(4)

    for row in dungeon.matrix:
        for room in row:
            print(room.position, end="")
        print()

    print(dungeon.matrix[0][1].position)

if __name__ == "__main__":
    main()
