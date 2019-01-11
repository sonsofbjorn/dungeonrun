import player


class Menu:
    while True:
        print("Välkommen till dungeonrun!\n"
              "[1] New Character\n"
              "[2] Load Character\n")

        menuchoice = input(">>")
        if menuchoice == "1":
            print("Please enter you Username")
            uname = input(">>")
            # function to check if name exists.
            print("Please choose your Class:\n"
                  "[1] Knight\n"
                  "[2] Wizard\n"
                  "[3] Thief")
            uclass = input(">>")
            if uclass == "1":
                uclass = "knight"
            elif uclass == "2":
                uclass = "wizard"
            elif uclass == "3":
                uclass = "thief"
            else:
                print("Incorrect input")
            if uclass.lower() == "wizard" or "knight" or "thief":
                user = player.Player(uname, uclass, "nw")
                # skicka vidare till en funktion

        elif menuchoice == "2":
            print("")

