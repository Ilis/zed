the_count = [1, 2, 3, 4, 5]
fruits = ["apple", "orange", "peach", "apricot"]
change = [1, "ten", 2, "fifty", 3, "handred"]

# 1st cycle
for number in the_count:
    print(f"Counter: {number}")

for fruit in fruits:
    print(f"Fruit: {fruit}")

for i in change:
    print(f"I've got a {i}")

# New list
elements = []

for i in range(0, 6):
    print(f"Add {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element is {i}")
