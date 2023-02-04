def set_array(n):
    ar = []
    for i in range(n):
      ar.append(float(input("\t" + str(i+1) + ': ')))
    return ar


if __name__ == '__main__':
    n = int(input("Введіть розмірність масиву "))
    print("Введіть масив")
    arr = set_array(n)
    print("Масив до змін\n\t" + str(arr))
    num = float(input("Введіть число "))
    for i in range(n):
        if arr[i] < num:
            arr[i] = num
    print("Масив після змін\n\t" + str(arr))






