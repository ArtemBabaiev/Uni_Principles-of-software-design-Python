from DoubleQueue import DoubleQueue
from random import randint

que = DoubleQueue()

for i in range(int(input("Введіть початкову кількість елементів: "))):
    que.push_back(randint(10, 99))

for item in que:
    print(f"{item}", end=" | ")
print()

que.push_front(1)
que.push_front(2)
que.pop_back()
que.push_back(999)

for item in que:
    print(f"{item}", end=" | ")
print()

print(f"Довжина {que.size}")
print(f"Перший елемент {que.front}")
print(f"Останній елемент {que.back}")
que.clear()
print(f"Довжина після видалення {que.size}")