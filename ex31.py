print("Let's play a game!")

print("You are in the dark room and you have 2 doors. Chose one")
door = input("> ")

if door == '1':
    print("There are huge bear in this room. What will you do?")
    print("1. Teese it")
    print("2. Argue it")

    bear = input("> ")
    if bear == '1':
        print("Well, bear bit your face")
    elif bear == '2':
        print("Well, bear bit your leg")
    else:
        print("Great! One and only right action. Bear ran away.")

elif door == '2':
    print("You faced Ctulchu. What will you do?")
    print("1. Told him about Siberia")
    print("2. Touch my jacket buttons")
    print("3. Sing him a song")

    ctulchu = input("> ")
    if ctulchu == '1' or ctulchu == '2':
        print("You resqued!")
    else:
        print("You fall into Ctulchu pool.")
else:
    print("You become insane")
