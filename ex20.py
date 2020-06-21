from sys import argv


script, input_file = argv


def print_all(f):
    print(f">>> print_all: {f = }")
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("Файл целиком:")
print_all(current_file)

print("Отмотаем назад, как кассету:")
rewind(current_file)

print("Выведем три строки:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 2
print_a_line(current_line, current_file)

current_line += 3
print_a_line(current_line, current_file)
