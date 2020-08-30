"""Школьный квест"""
from random import randrange


lesson_1 = False
canteen = False
lesson_2 = False
lesson_3 = False


def lesson_math():
    """Кабинет математики"""
    ...


def canteen():
    """Столовая"""
    ...


def lesson_cse():
    """Кабинет информатики"""
    ...


def lesson_pe():
    """Спортзал"""
    ...


def timetable():
    """Расписание"""
    print("""
=== Расписание уроков ===
| Математика            |
| Обед                  |
| Информатика           |
| Физ-ра                |
=========================
    """)


def hallway():
    """Коридор"""
    while True:
        print("\n=== Коридор ===\n")
        print("Справа от тебя висит расписание уроков, а дальше идут "
              "классы и другие помещения.")
        print("Смотреть расписание")
        print("Пойти в столовую")
        print("Пойти н спортзал")
        print("Пойти на математику")
        print("Пойти на информатику")

        choice = input("> ")
        if "смотр" in choice or "расп" in choice:
            timetable()
        elif "стол" in choice:
            canteen()
        elif "спорт" in choice:
            lesson_pe()
        elif "матем" in choice:
            lesson_math()
        elif "инфо" in choice:
            lesson_cse()
        else:
            print(f"Что значит «{choice}»? Реши, что делать дальше?")

        if lesson_3:
            break
    print("Ура, все уроки закончились! Завтра каникулы!")


def start():
    """Начало"""
    print("Ты зашёл в школу и оказался в коридоре.")
    hallway()


if __name__ == "__main__":
    start()
