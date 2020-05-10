print("Сколько тебе лет?", end=' ')
age = input()
print("Твой рост 1 м и сколько см?", end=' ')
height = int(input())
print("Твой вес?", end=' ')
weight = input()

print(f"Итак, тебе {age} лет, "
      f"в тебе {100 + height} см роста, "
      f"и ты весишь {weight} кг.")

# print("Введите a и b:")
# a = input() * 3
# b = int(input()) * 3
# print("a =", repr(a))
# print("b =", repr(b))
