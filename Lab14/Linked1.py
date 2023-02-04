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


class Linked1:

    def __init__(self):
        self.__head: Element = None
        self.__tail: Element = None
        self.__size: int = 0

    def __iter__(self):
        current = self.__head
        while current != None:
            yield current.Data
            current = current.Next

    def __len__(self):
        return self.__size
        # if self.__head == None:
        #     return 0
        # else:
        #     i = 0
        #     current = self.__head
        #     while current != None:
        #         i += 1
        #         current = current.Next
        #     return i

    def MyAddFirst(self, element):
        el = Element(element)
        el.Next = self.__head
        self.__head = el
        if self.__size == 0:
            self.__tail = self.__head
        self.__size += 1

    def MyAddLast(self, element):
        el = Element(element)
        if self.__head == None:
            self.__head = el
            self.__tail = el
        else:
            self.__tail.Next = el
        self.__tail = el
        self.__size += 1

    def MyAddAfter(self, after, toIsert) -> bool:
        el = Element(toIsert)
        current = self.__head
        while current != None:
            if current.Data == after:
                el.Next = current.Next
                current.Next = el
                self.__size += 1
                return True
            current = current.Next
        return False

    def MyRemove(self, element):
        current: Element = self.__head
        prev = None
        while current != None:
            if current.Data == element:
                if prev != None:
                    prev.Next = current.Next
                    if current.Next == None:
                        self.__tail = prev
                else:
                    self.__head = self.__head.Next
                    if self.__head == None:
                        self.__tail = None
                self.__size -= 1
                return
            prev = current
            current = current.Next
        return

    def MyRemoveFirst(self):
        if self.__head == None:
            return
        else:
            self.__head = self.__head.Next
            if self.__head == None:
                return
            else:
                self.__size -= 1

    def MyRemoveLast(self):
        current = self.__head
        prev: Element = None
        while True:
            if current.Next == None:
                break
            else:
                prev = current
                current = current.Next
        self.__tail = prev
        self.__tail.Next == None

    def MyClear(self):
        if self.__head == None:
            return
        self.__head.Next = None
        self.__head = None
        self.__tail = None
        self.__size = 0

    def MySearch(self, element: Element) -> bool:
        current: Element = self.__head
        while current != None:
            if current.Data == element.Data:
                return True
            current = current.Next
        return False
