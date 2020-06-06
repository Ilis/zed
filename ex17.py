from sys import argv
from os.path import exists


script, from_file, to_file = argv

print(f"Копирование данных из файла {from_file} в файл {to_file}.")
in_file = open(from_file)
in_data = in_file.read()

print(f"Исходный файл имеет размер {len(in_data)} символов.")

print(f"Целевой файл существует? {exists(to_file)}")
input("Готов копировать! Нажмите Enter для продолжения или Ctrl+C для отмены")

out_file = open(to_file, "w")
out_file.write(in_data)

print("Готово!")

out_file.close()
in_file.close()
