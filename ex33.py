numbers = []


def fill_numbers(stop, step):
    i = 0
    while i < stop:
        print(f"before {i = }")
        numbers.append(i)
        i += step
        print(f"{numbers = }")
        print(f"after {i = }")


fill_numbers(10, 2)

print("numbers:")
for number in numbers:
    print(number)
