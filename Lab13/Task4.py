from random import randint


def ranstr():
    temp = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y']
    for i in range(5):
        temp += letters[randint(0, len(letters) - 1)]
    return temp


def printAll(tpl: tuple):
    for sub in tpl:
        for el in sub:
            print(str(el).ljust(7), end="")
        print()


def printEl(tpl: tuple, num: int):
    print(f"{tpl[0][num]} | {tpl[1][num]} | {tpl[2][num]} | {tpl[3][num]}")


if __name__ == '__main__':
    Figures = tuple()
    num = int(input("Введіть кілкість учасників: "))
    tempArr = [[None for i in range(num)] for j in range(4)]
    average = 0
    for i in range(num):
        tempArr[0][i] = ranstr()
        temp = randint(1, 10) + randint(1, 10) / 10
        average += temp
        tempArr[1][i] = temp
        tempArr[2][i] = randint(16, 35)
        tempArr[3][i] = randint(10, 60)

    numOfPeople = 0
    average = round(average / num, 2)
    print(f"Середне значення: {average}")
    Figures = (tempArr[0], tempArr[1], tempArr[2], tempArr[3])
    printAll(Figures)
    for i in range(num):
        if Figures[1][i] > average:
            printEl(Figures, i)
            numOfPeople += 1
    print(f"Кваліфікацію пройшло {numOfPeople} людини")
