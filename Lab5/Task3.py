from random import randint


def sub_array(n):
    sar = []
    for j in range(n):
        sar.append(randint(-50, 50))
    return sar


def set_2d_array(n):
    ar = []
    for j in range(n):
      ar.append(sub_array(n))
    return ar


def print_2D(array2d):
    for array in array2d:
        print(array)


def over_main(arr, n):
    sumOfElements = 0
    for j in range(n-1):
        for k in range(j+1, n):
            sumOfElements += abs(arr[j][k])
    return sumOfElements


def under_main(arr, n):
    sumOfElements = 0
    for j in range(n-1):
        for k in range(j+1, n):
            sumOfElements += abs(arr[k][j])
    return sumOfElements


if __name__ == '__main__':
    size = int(input("Введіть розмірність масиву "))
    A = set_2d_array(size)
    print("Масив А")
    print_2D(A)
    x = []
    undmain = under_main(A, size)
    #print(undmain)
    ovmain = over_main(A, size)
    #print(ovmain)
    for i in range(size):
        if A[i][i] > 0:
            x.append(ovmain)
        if A[i][i] < 0:
            x.append(undmain)
    print("Векор X: " + str(x))
