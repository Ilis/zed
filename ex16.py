from sys import argv


_script, filename = argv

print(f"Я собираюсь стереть файл {filename}.")
print("Если его не надо стирать, нажмите Ctrl + C.")
print("Иначе нажмите Enter.")

input("?")

print("Открытие файла...")
target = open(filename, "w", encoding="utf-8")

print("Очистка файла...")
target.truncate()

print("Введите три строки.")
line1 = input("1: ")
line2 = input("2: ")
line3 = input("3: ")

print("Это я запишу в файл")
target.write(f"{line1}\n{line2}\n{line3}\n")

print("И закрою файл...")
target.close()
