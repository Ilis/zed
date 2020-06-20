def cheese_and_crackers(cheese_count, boxes_of_crackers):
    """Печатает количество сырков и чипсов, которых достаточно!"""
    print(f"У нас есть {cheese_count} сырков!")
    print(f"У нас есть {boxes_of_crackers} пачек чипсов!")
    print("Этого достаточно для вечеринки!\nПогнали!\n")


print("Мы можем передать числа")
cheese_and_crackers(20, 30)

print("Или мы можем передать переменные")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Мы можем выполнять вычисления")
cheese_and_crackers(10 + 20, 5 + 6)

print("И объединять переменные с числами")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("И как Вика попросила")
cheese_and_crackers(input("Сырков: "), input("Чипсов: "))
