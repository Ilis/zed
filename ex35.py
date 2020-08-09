def gold_room():
    print("Plenty of gold here. How much you want to get?")
    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Hey, it should be a number!")

    if how_much < 50:
        print("Good choice! You are not greedy, so you won!")
        exit(0)
    else:
        dead("You are so greedy!")


def bear_room():
    print("The bear sit here.")
    print("It has a pot of honey.")
    print("It locks the door.")
    print("How to move the bear?")
    print("Take its honey?")
    print("Ape him?")

    bear_moved = False

    while True:
        choice = input("take, ape or enter> ")

        if choice == "take":
            dead("Bear killed you!")
        elif choice == "ape" and not bear_moved:
            bear_moved = True
            print("Bear moved out of the door.")
        elif choice == "ape" and bear_moved:
            dead("Bear became angry and killed you!")
        elif choice == "enter" and bear_moved:
            gold_room()
        else:
            print(f"{choice} is not an option.")


def cthulhu_room():
    print("Cthulhu watching you.")
    print("You loose your mind.")
    print("What do you going to do?")
    choice = input("fight or run> ")

    if "run" in choice:
        start()
    elif "fight" in choice:
        dead("You can't win!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Great!")
    exit(0)


def start():
    print("You found yourself in a dark room.")
    print("There are two doors, left and right.")
    print("What door do you choose?")

    choice = input("left or right> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You didn't choose the door and die without food!")


start()
