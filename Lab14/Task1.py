from collections import deque
from Linked1 import Linked1
import re
import os


def clean_console(): return os.system('cls')


def Menu() -> float:
    print("1)	формування списку\n2)	перегляд елементів списку\n3)	визначення кількості елементів списку\n4)	перевірка списку на відсутність елементів")
    print("5)	вставка елементів в список\n6)	видалення елементів із списку\n7)	редагування елементів списку\n8)	заміна всіх елементів списку")
    print("9)	пошук елементів в списку за заданим полем\n10)	сортування елементів списку\n11)	збереження списку у файл\n12)	завантаження списку із файлу")
    op: float = float((input("Оберіть операцію: ")))
    if op == 5:
        print("1)	на початок\n2)	в кінець\n3)	у відповідну позицію")
        op += float((input("Оберіть опцію: ")))/10
    if op == 6:
        print(
            "1)	всіх елементів\n2)	конкретного елементу\n3)	елементу із заданим значенням\n")
        op += float(input("Оберіть опцію: ")) / 10.0
    return op


if __name__ == '__main__':
    repit: str = ""
    while repit != "N":
        clean_console()
        typ = int(
            input("1 - однозв'язний; 2 - двозв'язний\nВиберіть режим роботи: "))
        if typ == 1:
            Students = Linked1()
            while True:
                op: float = Menu()
                if op == 1.0:
                    Students.MyClear()
                    Students.MyAddLast("Бабаєв")
                    Students.MyAddLast("Вознюк")
                    Students.MyAddLast("Гатеж")
                    Students.MyAddLast("Давиденко")
                    Students.MyAddLast("Драгомирецька")
                    Students.MyAddLast("Житарю")
                    Students.MyAddLast("Кібак")
                    Students.MyAddLast("Клим")
                    Students.MyAddLast("Коваль")
                    Students.MyAddLast("Колотило")
                    Students.MyAddLast("Павлюк")
                    Students.MyAddLast("Прокопій")
                elif op == 2.0:
                    for item in Students:
                        print(f"{item} | ", end="")
                    print()
                elif op == 3.0:
                    print(f"Кількість елементів {len(Students)}")
                elif op == 4.0:
                    if (len(Students) == 0):
                        print("Ліст порожній")
                    else:
                        print("Ліст не порожній")
                elif op == 5.1:
                    Students.MyAddFirst(input("Введіть елемент: "))
                elif op == 5.2:
                    Students.MyAddLast(input("Введіть елемент: "))
                elif op == 5.3:
                    indexToIns = int(input("Введіть індекс для вставки: "))
                    elForAdding = input("Введіть елемент: ")
                    if indexToIns == 0:
                        Students.MyAddFirst(elForAdding)
                    elif indexToIns >= len(Students):
                        Students.MyAddLast(elForAdding)
                    else:
                        i = 0
                        for item in Students:
                            i += 1
                            if indexToIns == i:
                                Students.MyAddAfter(item, elForAdding)
                                break
                elif op == 6.1:
                    Students.MyClear()
                    print("Ліст очищено")
                elif op == 6.2:
                    index = int(
                        input(("Введіть індекс елементу для видалення: ")))
                    i = 0
                    for item in Students:
                        if i == index:
                            Students.MyRemove(item)
                            break
                        i += 1
                elif op == 6.3:
                    Students.MyRemove(input("Введіть елемент для видалення: "))
                elif op == 7.0:
                    size = len(Students)
                    print("Введіть нові елементи")
                    for i in range(size):
                        Students.MyRemoveFirst()
                        Students.MyAddLast(input())
                elif op == 8.0:
                    string = input("Ведіть слово для заміни: ")
                    size = len(Students)
                    for i in range(size):
                        Students.MyRemoveFirst()
                        Students.MyAddLast(string)
                elif op == 9.0:
                    toSearch = input("Ведіть слово для пошуку: ")
                    if Students.MySearch(toSearch):
                        print("Елемент наявний у списку")
                    else:
                        print("Елемент відсутній у списку")
                elif op == 10.0:
                    arr = []
                    for item in Students:
                        arr.append(item)
                    arr.sort()
                    for item in arr:
                        Students.MyRemoveFirst()
                        Students.MyAddLast(item)
                elif op == 11.0:
                    file = open("Linked1.txt", "w", encoding='utf_8')
                    for item in Students:
                        file.write(f"{item}\n")
                    file.close()
                elif op == 12.0:
                    file = open("Linked1.txt", "r", encoding='utf_8')
                    Students.MyClear()
                    arr = re.split(r"\n", file.read())
                    arr = arr[:-1]
                    for item in arr:
                        Students.MyAddLast(item)
                else:
                    break

        elif typ == 2:
            Goods = deque()
            size: int = 0
            while True:
                op: float = Menu()
                if op == 1.0:
                    Goods.clear()
                    Goods.append("book")
                    Goods.append("pencil")
                    Goods.append("pen")
                    Goods.append("ruller")
                    Goods.append("notebook")
                    Goods.append("pencilbox")
                    size = len(Goods)
                elif op == 2.0:
                    for el in Goods:
                        print(f"{el} | ", end="")
                    print()
                elif op == 3.0:
                    print(f"Кількість елементів {len(Goods)}")
                elif op == 4.0:
                    if (len(Goods) == 0):
                        print("Ліст порожній")
                    else:
                        print("Ліст не порожній")
                elif op == 5.1:
                    Goods.appendleft(input("Введіть елемент: "))
                elif op == 5.2:
                    Goods.append(input("Введіть елемент: "))
                elif op == 5.3:
                    indexToIns = int(input("Введіть індекс для вставки: "))
                    val: str = input("Що вставити: ")
                    size = len(Goods)
                    if indexToIns == 0:
                        Goods.appendleft(val)
                    elif indexToIns >= size:
                        Goods.append(val)
                    else:
                        Goods.insert(indexToIns, val)
                elif op == 6.1:
                    Goods.clear()
                    print("Ліст очищено")
                elif op == 6.2:
                    index = int(
                        input(("Введіть індекс елементу для видалення: ")))
                    i = 0
                    for item in Goods:
                        if i == index:
                            Goods.remove(item)
                            break
                        i += 1
                elif op == 6.3:
                    Goods.remove(input("Введіть елемент для видалення: "))
                elif op == 7.0:
                    size = len(Goods)
                    print("Введіть нові елементи")
                    for i in range(size):
                        Goods.popleft()
                        Goods.append(input())
                elif op == 8.0:
                    string = input("Ведіть слово для заміни: ")
                    size = len(Goods)
                    for i in range(size):
                        Goods.popleft()
                        Goods.append(string)
                elif op == 9.0:
                    toSearch = input("Ведіть слово для пошуку: ")
                    if Goods.count(toSearch) != 0:
                        print("Елемент наявний у списку")
                    else:
                        print("Елемент відсутній у списку")
                elif op == 10.0:
                    arr = []
                    for item in Goods:
                        arr.append(item)
                    arr.sort()
                    for item in arr:
                        Goods.popleft()
                        Goods.append(item)
                elif op == 11.0:
                    file = open("Linked2.txt", "w")
                    for item in Goods:
                        file.write(f"{item}\n")
                    file.close()
                elif op == 12.0:
                    file = open("Linked2.txt", "r")
                    Goods.clear()
                    arr = re.split(r"\n", file.read())
                    arr = arr[:-1]
                    for item in arr:
                        Goods.append(item)
                else:
                    break
        repit = input("Введіть N для закінчення: ")
