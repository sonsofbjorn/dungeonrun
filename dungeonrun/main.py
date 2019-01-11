from dungeonrun import player
from dungeonrun import dungeon


def main():
    print("run something")


if __name__ == "__main__":
    main()


dungeon = dungeon.Map(4)

dude = player.Player("Bob", "knight", dungeon.matrix[0][0])

dude.show_location()

newRoom = dungeon.enterDoor(dude.position, "north")

dude.move_character(newRoom)

