if __name__ == '__main__':

    n = int(input("Введіть N: "))
    a = float(input("ВВедіть а: "))

    if a != 0 and a != -n:

        denominator = a
        sum = 0
        for i in range(n):
            numerator = 2*(i+1)
            sum += numerator/denominator
            denominator *= (a+(i+1))
        print("Сума: " + str(sum))
    elif a == 0:
        print("Число а = 0")
    elif a == -n:
        print("знаменик на n-ому кроці = 0")