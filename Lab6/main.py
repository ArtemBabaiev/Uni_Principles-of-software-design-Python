import random


def set_array(n):
    arr = []
    for i in range(n):
      arr.append(random.randint(-49, 50))
    return arr


def print_array(arr, size):
    for i in range(size):
        print(str(arr[i]).ljust(3) + " | ", end="")
        if i == 19 or i == 39 or i == 59 or i == 79 or i == 99:
            print()

# 1
def bubble_sort(arr, size):
    for i in range(size-1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

# 2
def shaker_sort(arr, size):
    lstart = 0
    rstart = size - 1
    while (lstart < rstart):
        for i in range(lstart, rstart, 1):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
        rstart -= 1
        for i in range(rstart, lstart, -1):
            if arr[i] < arr[i - 1]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        lstart += 1

# 3
def insertion_sort(arr, size):
    for i in range(1, size, 1):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

# 4
def stooge_sort(arr, start_index, end_index):
    if arr[start_index] > arr[end_index]:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        if end_index - start_index > 1:
            size = (end_index - start_index + 1) / 3
            stooge_sort(arr, start_index, end_index - size)
            stooge_sort(arr, start_index + size, end_index)
            stooge_sort(arr, start_index, end_index - size)

# 5
def shell_sort(arr, size):         # 5
    step = size
    while step > 1:
        step = int(step/2)
        for i in range(step, size):
            for j in range(i,step-1, -step):
                if arr[j - step] > arr[j]:
                    arr[j - step], arr[j] = arr[j], arr[j - step]

# 6
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        LeftPart = arr[:mid]
        RightPart = arr[mid:]

        merge_sort(LeftPart)
        merge_sort(RightPart)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(LeftPart) and j < len(RightPart):
            if LeftPart[i] < RightPart[j]:
                arr[k] = LeftPart[i]
                i += 1
            else:
                arr[k] = RightPart[j]
                j += 1
            k += 1

        while i < len(LeftPart):
            arr[k] = LeftPart[i]
            i += 1
            k += 1

        while j < len(RightPart):
            arr[k] = RightPart[j]
            j += 1
            k += 1

# 7
def selection_sort(arr, size):         # 7
    for i in range(size-1):
        smallestElementIndex = i
        for j in range(i+1, size):
            if arr[j] < arr[smallestElementIndex]:
                smallestElementIndex = j
        arr[smallestElementIndex], arr[i] = arr[i], arr[smallestElementIndex]

# 8
def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


if __name__ == '__main__':
    length = 100
    A = set_array(length)
    B = set_array(length)
    print("Масив А")
    print_array(A, length)
    print("Масив В")
    print_array(B, length)
    repit = True
    while repit:
        print("1 -Бульбашка, 2 - Шейкерне, 3 - Вставками, 4 - Частинами")
        print("5 - Шелл, 6 - Злиття, 7 - Вибором, 8 - Гоара")
        num = int(input("Введіть номер сортування: "))
        print("___________________________________Start__________________________________\n")
        if num == 1:
            print("Сортування бульбашкою ")
            duplicate = A
            bubble_sort(A, length)
            print_array(A, length)
            A = duplicate
        elif num == 2:
            print("Шейкерне сортування")
            duplicate = A
            shaker_sort(A, length)
            print_array(A, length)
            A = duplicate
        elif num == 3:
            print("Сортування вставками")
            duplicate = A
            insertion_sort(A, length)
            print_array(A, length)
            A = duplicate
        elif num == 4:
            print("Сортування частинами")
            duplicate = A
            stooge_sort(A, 0, length-1)
            print_array(A, length)
            A = duplicate
        elif num == 5:
            print("Сортування Шелла ")
            duplicate = B
            shell_sort(B, length)
            print_array(B, length)
            B = duplicate
        elif num == 6:
            print("Сортування злиттям ")
            duplicate = B
            merge_sort(B)
            print_array(B, length)
            B = duplicate
        elif num == 7:
            print("Сортування вибором ")
            duplicate = B
            selection_sort(B, length)
            print_array(B, length)
            B = duplicate
        elif num == 8:
            print("Cортування Гоара ")
            duplicate = B
            B = quick_sort(B)
            print_array(B, length)
            B = duplicate
        else:
            repit = False
        print("___________________________________End__________________________________\n")
