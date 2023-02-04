if __name__ == '__main__':

    eps = float(input("Введіть epsilon: "))

    x = 1
    sumOfElements = 0
    while x <= 5:
        k = 0
        fact = 1
        oneToK = -1
        numerator = oneToK * pow(x, 2 * k - 1)
        denominator = (2 * k + 1) * fact
        element = numerator / denominator
        while abs(element) > eps:
            # print(x, " | ", k, " | ", element)
            sumOfElements += element
            k += 1
            fact *= k
            oneToK *= -1
            numerator = oneToK * pow(x, 2 * k - 1)
            denominator = (2 * k + 1) * fact
            element = numerator / denominator
        x += 1
    print("Сума дорівнює: " + str(sumOfElements))
