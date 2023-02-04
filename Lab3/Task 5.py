if __name__ == '__main__':

    massOfGrain = float(input("Введіть масу однієї зернини: "))

    n = 1
    sumOfGrains = 1
    print("1 ячейка", " | ", n, )
    for i in range(63):
        n *=2
        sumOfGrains += n
        print((i+2), "ячейка | ", n, " | ")
    print("\nЗагальна кількість зерен ", sumOfGrains)
    print("Маса зерна: ", massOfGrain*sumOfGrains)

