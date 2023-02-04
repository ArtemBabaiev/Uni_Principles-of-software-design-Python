import warnings
warnings.filterwarnings("ignore")
import re
import codecs

toExit = "no"
while toExit != "exit":
    file = open('expression.txt', 'w')
    file.close()
    print("\nВведіть вираз до файлу та збережіть файл")
    toCont = "no"
    while toCont != "continue":
        toCont = input('''Введіть "continue" для продовження: ''')
    file = open('expression.txt', 'r')
    expr = file.readline()
    file.close()
    if len(expr) != 0:
        arr = re.findall(r"[^0-9\+\-\/\*\(\)]", expr)
        file = codecs.open('expression.txt', 'a', 'utf-8')
        if len(arr)!=0:
            print("У виразі містяться недопустимі символи")
            file.close()
        else:
            openD = re.findall(r"\(", expr)
            closeD = re.findall(r"\)", expr)
            if len(openD) != len(closeD):
                print("Кілкість відкриваючих та закриваючих дужок різна")
            elif len(re.findall(r"[\*\/][\*\/]", expr)) != 0:
                print("Некоректне використання символів * та /")
            else:
                try:
                    result = eval(expr)
                except TypeError:
                    print("Не коректно записано вираз")
                except ZeroDivisionError:
                    print("Ділення на нуль неможливе")
                    file.write("\nРезультат не визначений")
                else:
                    print("Результат занесено до файлу")
                    file.write("\nРезультат = %s" % result)
                finally:
                    file.close()
    else:
        print("Вираз не введено")
    toExit = input('''Введіть "exit" для виходу: ''')