from abc import ABC, abstractmethod
import datetime
from random import randint
class Animal(ABC):
    def __init__(self, name:str = "default", breed:str = "default", wasInVet:bool = False):
        self._name = name
        self._breed = breed
        self._wasInVet = bool(wasInVet)
        if wasInVet:
            self._date = datetime.date(randint(2000, 2021), randint(1, 12), randint(1, 28))

    @abstractmethod
    def Command(self):
        pass
    @abstractmethod
    def Call(self):
        pass
    
    @property
    def DateOfVet(self):
        if self._wasInVet:
            return str(self._date)
        else:
            return "Ніколи не була"
    
    def Show(self):
        print("Name: {name} | Breed: {breed} | DateOfVet: {Date} | ".format(name=self._name, breed = self._breed, Date = self.DateOfVet), end="")

class Dog(Animal):
    def __init__(self, isHunt:bool = False ,name:str = "default", breed:str = "default", wasInVet:bool = False):
        Animal.__init__(self, name, breed, wasInVet)
        self.__isHunt = bool(isHunt)
    def Command(self, command:str):
        print("{name} зробив команду {com}".format(name=self._name, com = command))
    def Call(self, phrase:str):
        print("*махає хвостом")
    def Show(self):
        Animal.Show(self)
        print("Придатна до полювання: {forHunt} | ".format(forHunt=self.__isHunt))
    def Bark(self):
        print("BARK")

class Cat(Animal):
    def __init__(self, mass:int = -1 ,name:str = "default", breed:str = "default", wasInVet:bool = False):
        Animal.__init__(self, name, breed, wasInVet)
        self.__mass = mass
    
    def Call(self, name:str):
        if name == self._name:
            print("*відізвався")
        else:
            print("*нічого не сталося")
    def Command(self, command):
        print("*ігнорує")
    
    def Show(self):
        Animal.Show(self)
        print("Масса: {mass} | ".format(mass=self.__mass))
    
    def Meow(self):
        print("MEOW")

if True:
    arr = []
    n = int(input("Кільскість тварин: "))
    for i in range(n):
        choice = int(input("1 - Собака | 2 - Кіт: "))
        if choice == 1:
            arr.append(Dog(randint(0, 1), input("Ім'я: "), input("Порода: "), randint(0, 1)))
        else:
            arr.append(Cat(randint(2, 20), input("Ім'я: "), input("Порода: "), randint(0, 1))) 
    
    for i in range(len(arr)):
        arr[i].Show()
        print(125*"*")
    print("***********************Пошук***********************")
    forSearch = input("Ввеідть дату у форматі рррр-мм-дд: ")
    j = 0
    for el in arr:
        if str(el.DateOfVet) == forSearch:
            el.Show()
            j += 1
    if j==0:
        print("Таких немає")
    print(125*"*")
    dog = Dog(True, "ho", "hi", True)
    cat = Cat(45, "ki", "ko", False)
    cat.Call("ki")
    cat.Call("ko")
    cat.Command("sit")
    dog.Call("body")
    dog.Command("sit")   
