if __name__ == '__main__':
    radius = float(input("Введіть радіус: "))
    table = "№".center(3, '_') + '|' + "Координати".center(13, '_') + '|' + "Результат".center(12, '_') + '|\n'
    for i in range(10):
        print(str(i+1) + "-й постріл")
        x = int(input("\tx = "))
        y = int(input("\ty = "))
        radiusToPoint = x ** 2 + y ** 2
        if ((x >= 0 and y >= 0) or (x < 0 and y < 0)) and radiusToPoint <= radius ** 2:
            if abs(y) >= abs(x):
                    table = table + str(i+1).center(3, '_') + '|'
                    table = table + str(x).rjust(6, '_') + ';' + str(y).ljust(6, '_') + '|'
                    table = table + "Влучив".center(12, '_') + "|\n"
            else:
                table = table + str(i + 1).center(3, '_') + '|'
                table = table + str(x).rjust(6, '_') + ';' + str(y).ljust(6, '_') + '|'
                table = table + "Не влучив".center(12, '_') + "|\n"
        else:
            table = table + str(i + 1).center(3, '_') + '|'
            table = table + str(x).rjust(6, '_') + ';' + str(y).ljust(6, '_') + '|'
            table = table + "Не влучив".center(12, '_') + "|\n"
    print(table)
