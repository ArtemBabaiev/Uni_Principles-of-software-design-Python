from collections import namedtuple
from random import randint


def ranstr():
    temp = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y']
    for i in range(5):
        temp += letters[randint(0, len(letters) - 1)]
    return temp


def good_pupils(tpl: tuple):
    average = 0
    for i in range(7):
        average += tpl[i].mark
    average /= 7
    arr = []
    for i in range(7):
        if tpl[i].mark >= average:
            arr.append(tpl[i].name)
    if len(arr) == 0:
        print("Ніхто добре не вчиться")
    else:
        print(f"Учні {arr} в цьому семестрі добре вчаться!")


if __name__ == '__main__':
    lst = ['name', 'age', 'mark', 'adress']
    Pupil = namedtuple('Pupil', lst)
    people = tuple(Pupil(ranstr(), randint(7, 17), randint(1, 12), ranstr() + str(randint(1, 25))) for i in range(7))
    good_pupils(people)
    people2 = list()
    for i in range(7):
        people2.append(people[i]._replace(mark=5))
    people2 = tuple(people2)
    good_pupils(people2)
