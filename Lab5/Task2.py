from random import randint


def set_array(n):
    ar = []
    for k in range(n):
      ar.append(randint(-3, 10))
    return ar


if __name__ == '__main__':
    arr = set_array(20)
    print("Масив до змін\n\t" + str(arr))
    for i in range(0, 20):
        if arr[i] > 0:
            for j in range(20):
                if arr[i] == -arr[j]:
                    arr[j] = -arr[j]
    print("Масив після змін\n\t" + str(arr))
