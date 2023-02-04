if True:
    print("\nПідзавдання 1")
    name = input('''Введіть ім'я: ''')
    #print("Привіт, %s" % name)
    print("Привіт, {0}".format(name))

    print("\nПідзавдання 2")
    result = ""
    string1 = input('''Введіть рядок: ''')
    string2 = input('''Введіть рядок: ''')
    result = string1[:2] + string2[len(string2) - 1]
    print("Резульат %s" % result)

    print("\nПідзавдання 3")
    apple = "Яблуко"
    result3 = apple[1:3] + apple[len(apple)-1: -3: -1]
    print(result3)
    
    print("\nПідзавдання 4")
    string4 = input("Введіть рядок: ")
    result4 = string4.replace(" ", "_")
    print(result4)
    