def add(a, b):
    print(f"add {a} and {b}")
    return a + b


def subtract(a, b):
    print(f"subtract {a} and {b}")
    return a - b


def multiply(a, b):
    print(f"multiply {a} and {b}")
    return a * b


def divide(a, b):
    print(f"divide {a} and {b}")
    return a / b


print("Let's do some operations")

age = add(40, 4)
height = subtract(200, 24)
weight = multiply(20, 4)
iq = divide(220, 2)

print(f"{age = }; {height = }; {weight = }; {iq = }")

print("This is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("Result is", what, "really?")
