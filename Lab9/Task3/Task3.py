import warnings
warnings.filterwarnings("ignore")
import re
import codecs
toExit = "no"
while toExit != "exit":
    file = open('expression.txt', 'w')
    file.close()
    print("Введіть вираз до файлу та збережіть файл")
    toCont = "no"
    while toCont != "continue":
        toCont = input('''\nВведіть "continue" для продовження: ''')
    file = open('expression.txt', 'r')
    expr = file.readline()
    file.close()
    if len(expr) != 0:
        if len(re.findall(r"[^0-9\+\-\/\*]", expr)) != 0:
            print("У виразі містяться недопустимі символи")
            file.close()
        else:
            if len(re.findall(r"[\+\-\/\*]", expr)) == 0:
                print("Знак операції пропущенo")
            elif len(re.findall(r"[\+\-\/\*]", expr)) > 1:
                print("Вираз повинен містити одну операцію")
            else:
                file = codecs.open('expression.txt', 'a', 'utf-8')
                result = None
                if "+" in expr:
                    result = int(expr[0:expr.index("+")]) + int(expr[expr.index("+")+1:])
                elif "-" in expr:
                    result = int(expr[0:expr.index("-")]) - int(expr[expr.index("-")+1:])
                elif "*" in expr:
                    result = int(expr[0:expr.index("*")]) * int(expr[expr.index("*")+1:])
                elif "/" in expr:
                    try:
                        result = int(expr[0:expr.index("/")]) / int(expr[expr.index("/")+1:])
                    except ZeroDivisionError:
                        print("Ділення на нуль неможливе")
                        result = None
                if result == None:
                    file.write("\nРезультат не визначений")
                else:
                    print("Результат занесено до файлу")
                    file.write("\nРезультат = %s" % result)
                file.close()
    else:
        print("Вираз не введено")
    toExit = input('''Введіть "exit" для виходу: ''')
    
                    
                