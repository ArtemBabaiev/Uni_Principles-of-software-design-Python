def set_array(n):
    arr = []
    for k in range(n):
      arr.append(int(input()))
    return arr


def print_2d(array2d):
    for array in array2d:
        print(array)


if __name__ == '__main__':
    outer = int(input("Введіть розмір зовнішнього масиву: "))
    Task6Array = []
    Indexes = []
    Result = []
    for i in range(outer):
        inner = int(input("Введіть розмір " + str(i+1) + " підмасиву: "))
        while inner < 1 or inner > outer:
            inner = int(input("Введіть розмір " + str(i + 1) + " підмасиву: "))
        Indexes.append(inner)
        print("Введіть елементи")
        Task6Array.append(set_array(inner))
    print("Східчастий масив:")
    print_2d(Task6Array)

    maxind = max(Indexes)
    for i in range(maxind):
        minEl = 2147483647
        for j in range(outer):
            ok = True
            try:
                Task6Array[j][i] = Task6Array[j][i]
            except IndexError:
                continue
            else:
                if Task6Array[j][i] < minEl:
                    minEl = Task6Array[j][i]
        Result.append(minEl)
    print("\nМінімальні елементи: " + str(Result))