import random
import re

if True:
    file1 = open('TF_1.txt', 'w')
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ', ',', '.', ';', ':', '_', '\n']
    num = int(input("Введіть кількість символів: "))
    for i in range(num + 1):
        file1.write(letters[random.randint(0, len(letters)-1)])
    file1.close()
    file1 = open('TF_1.txt', 'r')
    text1 = file1.read()
    file1.close()
    words = re.split(r"[ _\.\,\;\:]", text1)
    file2 = open('TF_2.txt', 'w')
    for word in words:
        if word == "\n":
            file2.write("\n")
        else:
            file2.write(word + "\n")
    file2.close()
    file2 = open('TF_2.txt', 'r')
    strings = file2.readlines()
    file2.close()
    print("Вміст файлу TF_2")
    for el in strings:
        print("\t%s" % el, end="")