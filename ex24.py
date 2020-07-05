print("Давайте попрактикуемся")
print("Экранирование\\")
print("Перенос\nстрок и\tтабуляция")

poem = """\tПоэт
Я — поэт
Зовусь я Цветик
От меня вам всем приветик
\t\tЦветик"""

print("-" * 20)
print(poem)
print("-" * 20)

five = 2**2 + 1
print(f"Five to be here: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans // 100
    crates = jars // 2
    return jelly_beans, jars, crates


start_point = 10_000
beans, jars, crates = secret_formula(start_point)

# Comments
formula = secret_formula(start_point)
print("Starting with: {}".format(start_point))
print("We have {} beans, {} jars and {} crates.".format(*formula))
