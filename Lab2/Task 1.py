if __name__ == '__main__':

    print("\n__________________________________________part 1______________________________\n")
    radius = abs(int(input("Введіть довжину радіуса: ")))
    x = float(input("Введіть x-ву координату точки: "))

    y = float(input("Введіть y-ву координату точки: "))

    radiusToPoint = x**2+y**2
    if ((x >= 0 and y >= 0) or (x < 0 and y < 0)) and radiusToPoint <= radius**2:
        if abs(y) >= abs(x):
            if radiusToPoint < radius**2:
                print("Так")
            if (x == y) or (x == 0) or radiusToPoint == radius**2:
                print("На межі")
        else:
            print("Ні")
    else:
        print("Ні")

