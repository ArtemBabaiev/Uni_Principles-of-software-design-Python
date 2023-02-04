from random import randrange


def sub_array(sub_size):
    sar = []
    for k in range(sub_size):
        #sar.append(int(input("Зарплатат за " + str(k+1) + " місяць ")))
        sar.append(randrange(100, 1000, 100))
    return sar


def set_2d_array(main_size, sub_size):
    arr = []
    for j in range(main_size):
        #print(str(j + 1) + " людина")
        arr.append(sub_array(sub_size))
    return arr


def print_2D(array2d):
    for array in array2d:
        print(array)


if __name__ == '__main__':
    numberOfEmployees = 18
    numberOfMonths = 12
    salary = set_2d_array(numberOfEmployees, numberOfMonths)
    print(["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"])
    print_2D(salary)
    sumOfAll = 0
    sumOfAprils = 0
    for array in salary:
        i=0
        for elem in array:
            sumOfAll += elem
            if i == 3:
                sumOfAprils += elem
            i += 1
    averegaForApril = round(sumOfAprils/numberOfEmployees, 2)
    print("Загальний бюджет " + str(sumOfAll))
    print("Загально за квітень " + str(sumOfAprils))
    print("Середнє за квітень " + str(averegaForApril))

