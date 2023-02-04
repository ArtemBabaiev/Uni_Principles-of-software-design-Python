import math


def areaOfTriangle(a, b, c):
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s


if __name__ == '__main__':
    a1 = int(input("Введіть довжину першої сторони "))
    a2 = int(input("Введіть довжину другої сторони "))
    a3 = int(input("Введіть довжину третьої сторони "))
    if (a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1):
        print("Площа трикутника " + str(areaOfTriangle(a1, a2, a3)))
    else:
        print("Такого трикутника не існує")


