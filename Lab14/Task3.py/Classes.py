class ShopMan():
    def __init__(self, name: str, howMuch: int):
        self.__name = name
        self.__Cart = []
        self.__numToBuy = howMuch

    def __ListStr(self):
        string = ""
        for item in self.__Cart:
            string += item + " "

    def __str__(self):
        return f"Ім'я: {self.__name} | Список: {self.__ListStr()}"

    @property
    def Name(self):
        return self.__name

    @property
    def NumToBuy(self):
        return self.__numToBuy

    def AddToCart(self, item: str):
        self.__numToBuy -= 1
        self.__Cart.append(item)


class Element:
    __data = None
    __next = None

    def __init__(self, current):
        self.__data = current

    @property
    def Data(self):
        return self.__data

    @Data.setter
    def Data(self, value):
        self.__data = value

    @property
    def Next(self):
        return self.__next

    @Next.setter
    def Next(self, value):
        self.__next = value


class LoopList():
    def __init__(self):
        self.__head: Element = None
        self.__tail: Element = None
        self.__size: int = 0

    def __iter__(self):
        current = self.__head
        while (True):
            if (current != None):
                yield current.Data
                current = current.Next

    def Add(self, element):
        ElNew = Element(element)
        if self.__head == None:
            self.__head = ElNew
            self.__tail = ElNew
            self.__tail.Next = self.__head
        else:
            ElNew.Next = self.__head
            self.__tail.Next = ElNew
            self.__tail = ElNew
        self.__size += 1

    def PrintShoppers(self):
        print(str(self.__head.Data))
        current = self.__head.Next
        while current != self.__head:
            print(str(current.Data))
            current = current.Next
