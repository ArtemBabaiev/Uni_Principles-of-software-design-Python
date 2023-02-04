class DoubleQueue():
    __lst: list

    def __init__(self):
        self.__lst = []

    def push_front(self, el):
        self.__lst.insert(0, el)

    def push_back(self, el):
        self.__lst.append(el)

    def pop_front(self):
        return self.__lst.pop(0)

    def pop_back(self):
        return self.__lst.pop()

    def clear(self):
        self.__lst.clear()
    @property
    def front(self):
        return self.__lst[0]

    @property
    def back(self):
        return self.__lst[self.size-1]

    @property
    def size(self):
        return len(self.__lst)

    def __iter__(self):
        for item in self.__lst:
            yield item
