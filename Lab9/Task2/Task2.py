import random

file1 = open('file_1.txt', 'w')
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '\n', '(', ')']
num = int(input("Введіть кількість символів: "))
for i in range(num + 1):
    file1.write(letters[random.randint(0, len(letters) - 1)])
file1.close()
file1 = open('file_1.txt', 'r')
strings = file1.readlines()
file1.close()
file2 = open('file_2.txt', 'w')
for i in range(len(strings)):
    strings[i] = strings[i].replace("(", "*")
    strings[i] = strings[i].replace(")", "#")
    file2.write(strings[i])
print("End")
