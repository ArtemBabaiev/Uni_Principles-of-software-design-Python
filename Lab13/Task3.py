from enum import Enum


class Book(Enum):
    The_Godfather = 1969
    The_Hobbit = 1937
    The_Lord_of_Rings_1 = 1954.07
    The_Lord_of_Rings_2 = 1954.11
    The_Lord_of_Rings_3 = 1955
    The_Silmarillion = 1977
    The_Children_of_Hurin = 2007
    Beren_and_Luthien = 2017
    The_Fall_of_Gondolin = 2018

    @staticmethod
    def all_info(name):
        name = name.replace(" ", "_")
        print(f"{name}: {Book[name].value}")

    @staticmethod
    def one_info(isName: bool):
        if isName:
            for el in Book:
                print(el.name, end=" | ")
            print()
        else:
            for el in Book:
                print(el.value, end=" | ")
            print()


if __name__ == '__main__':
    Book.all_info("The Godfather")
    Book.one_info(True)
    Book.one_info(False)
