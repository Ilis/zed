people = 30
cars = 40
trucks = 15

if cars > people:
    print("Let's take a car")
elif cars < people:
    print("Do not take a car")
else:
    print("Can't choose")

if trucks > cars:
    print("Too mach trucks")
elif trucks < cars:
    print("May be trucks?")
else:
    print("Still can't choose")

if people > trucks:
    print("OK, let's take a truck")
else:
    print("Well, let's be at home")
