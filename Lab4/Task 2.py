import math


def func(x, y, i):
    if x > y:
        f = x**3 + math.sqrt(x**2+y**4)
    else:
        if x>0:
            f = (x**2-2*x + x**0.5)/(x**(3/5))
        else:
            print("Першу операію пропущенно через x = 0 або x < 0")
            i += 1
            return func(2, x, i) + 2
    if i == 1:
        return f
    i += 1
    return f + func(2, x, i) + 2


if __name__ == '__main__':
    a = int(input("Введіть a "))
    b = int(input("Введіть b "))
    u = func(a, b, 0)
    print("Значення виразу: " + str(u))
