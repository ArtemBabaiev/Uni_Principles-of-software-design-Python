import re

string = "qwerty 18.07.2002 asdfg18,07.2002 asd 18u07.2002 qse 18.07.2020"
print(string)
result = re.findall(r"[0-3][0-9]\.[0-1][0-9]\.[1-2][90][0-9][0-9]", string)
print("Знайшли %s" % result)
print("Кількість %s" % len(result))

for i in range(len(result)):
    print("\nСпівпадіння: %s" % result[i])
    print("0-Залишити\n1-Вилучити\n2-Замінити")
    choice = int(input("Вибір: "))
    if choice == 0:
        continue
    elif choice == 1:
        string = string.replace(result[i], "")
    elif choice == 2:
        string = string.replace(result[i], input("Введіть заміну: "))
print("\n%s" % string)


