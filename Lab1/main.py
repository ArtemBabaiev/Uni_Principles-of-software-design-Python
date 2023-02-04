if __name__ == '__main__':
    import math
    print("\n_________________________________part 1______________________________________\n")
    print("Введіть координати точки А")
    ax = float(input("x = "))
    ay = float(input("y = "))
    print("\nВведіть координати точки B")
    bx = float(input("x = "))
    by = float(input("y = "))
    print("\nВведіть координати точки C")
    cx = float(input("x = "))
    cy = float(input("y = "))

    AB = math.sqrt((math.pow(ax-bx, 2) + math.pow(ay-by, 2)))
    AC = math.sqrt((math.pow(ax-cx, 2) + math.pow(ay-cy, 2)))
    BC = math.sqrt((math.pow(cx - bx, 2) + math.pow(cy - by, 2)))

    halfPerimeter = (AB+BC+AC)/2
    areaOfTriangle = (halfPerimeter * (halfPerimeter - AB) * (halfPerimeter - AC) * (halfPerimeter - BC)) ** 0.5
    print("\nArea of triangle is ", areaOfTriangle)

    print("\n_________________________________part 2______________________________________\n")
    x1 = float(input("Введіть х1: "))
    x2 = float(input("Введіть х2: "))
    y = math.sqrt(math.pow(x1, 3) + math.pow(x2, 5)) / 1000 + 65
    print(y)

    print("\n_________________________________part 3______________________________________\n")
    alpha = math.radians(float(input("Enter Alpha ")))
    z1 = math.cos(alpha) + math.sin(alpha) + math.cos(3*alpha) + math.sin(3*alpha)
    print("z1 = " + str(z1))
    z2 = 1/4 -(1/4)*math.sin((5/2)*math.pi -8*alpha)
    print("z2 = " + str(z2))