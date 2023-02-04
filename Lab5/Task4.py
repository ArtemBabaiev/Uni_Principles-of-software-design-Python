from random import randint


def sub_array(m):
    sar=[]
    for k in range(m):
        sar.append(randint(-50, 50))
    return sar


def set_2d_array(n, m):
    arr = []
    for j in range(n):
        arr.append(sub_array(m))
    return arr



def print_2D(array2d):
    for array in array2d:
        print(array)


if __name__ == '__main__':
    main_size=5
    sub_size=4
    A = set_2d_array(main_size, sub_size)
    print("Масив А")
    print_2D(A)
    maxElement = -1
    print("*******************************")
    for i in range(main_size):
        for j in range(sub_size):
            if abs(A[i][j]) >= maxElement:
                maxElement = abs(A[i][j])
                maxI = i
                maxJ = j
    print("Максимальний елемент: " + str(maxElement))
    print("Координати: " + str(maxJ) + ";" + str(maxI))