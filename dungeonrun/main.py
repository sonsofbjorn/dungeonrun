from dungeon import Map


def main():
    dungeon = Map(4)

    print("=== MAIN ===")
    for rooms in dungeon:
        for room in rooms:
            print(room.doors, end="")
        print()


if __name__ == "__main__":
    main()
