def vec(ar1, ar2, n, j):
    if j < n:
     product = ar1[j]*ar2[j]
    else:
        return 0
    return product + vec(ar1, ar2, n, j+1)


def set_array(n):
    ar = []
    for i in range(n):
      ar.append(int(input("\t" + str(i+1) + ': ')))
    return ar


if __name__ == '__main__':
    n = int(input("Введіть вимір: "))
    print("Введіть координати вектора а: ")
    a = set_array(n)
    print("Введіть координати вектора b: ")
    b = set_array(n)
    print("Введіть координати вектора c: ")
    c = set_array(n)

    print("A = " + str(a))
    print("B = " + str(b))
    print("C = " + str(c))

    print("Скалярний добуток: " + str(2*vec(a, b, n, 0) - 3*vec(a, c, n, 0)))









# def vec(ar1, ar2, n):
#     product = 0
#     for j in range(n):
#         product += ar1[j]*ar2[j]
#     return product