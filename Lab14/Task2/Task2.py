import re


def Show(li: list):
    for item in li:
        print(f"{item}", end=" | ")
    print()


def ListToStr(li: list) -> str:
    string = ""
    i = 0
    j = 0
    for item in li:
        string += str(item)
        i += 1
        j += 1
        if i == 8:
            i = 0
            string += "\n"
            continue
        if j == len(li):
            continue
        string += " "
    return string


if __name__ == '__main__':

    file1 = open("L1.txt", "w")
    file2 = open("L2.txt", "w")
    file1.close()
    file2.close()

    file1 = open("L1.txt", "r")
    file2 = open("L2.txt", "r")
    L1 = []
    L2 = []
    inp = ""
    while inp != "exit":
        inp = input(
            "Введіть елементи списку до файлів\nДля продовження введіть exit: ")
    temp = re.split(r" ", file1.read())
    for item in temp:
        L1.append(int(item))
    L1.sort(reverse=True)
    temp = re.split(r" ", file2.read())
    for item in temp:
        L2.append(int(item))
    file1.close()
    file2.close()
    Show(L1)
    Show(L2)
    for item in L2:
        isInserted: bool = False
        for i in range(len(L1)):
            if item >= L1[i]:
                L1.insert(i, item)
                isInserted = True
                break
        if not isInserted:
            L1.append(item)
    file = open("Result.txt", "w")
    file.write(ListToStr(L1))
    file.close()
