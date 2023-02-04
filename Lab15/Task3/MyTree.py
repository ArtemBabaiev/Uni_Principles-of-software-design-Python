class Node():
    def __init__(self, data: str):
        self.__data: str = data
        self.__right: Node = None
        self.__left: Node = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value


class Tree():
    def __init__(self) -> None:
        self.__head: Node = None

    def add(self, el: str) -> bool:
        toAdd = Node(el)
        if self.__head == None:
            self.__head = toAdd
            return True
        else:
            prev: Node = None
            current = self.__head
            path = ""
            while current != None:
                if toAdd.data > current.data:
                    prev = current
                    current = current.right
                    path = "Right"
                elif (toAdd.data < current.data):
                    prev = current
                    current = current.left
                    path = "Left"
                else:
                    return False
            if path == "Right":
                prev.right = toAdd
            elif (path == "Left"):
                prev.left = toAdd
            return True

    def search(self, el: str) -> bool:
        current = self.__head
        while current != None:
            if el > current.data:
                current = current.right
            elif (el < current.data):
                current = current.left
            elif el == current.data:
                return True
        return False

    def remove(self, el: str) -> bool:
        if self.__head == None:
            return False
        else:
            current = self.__head
            prev: Node = None
            path = ""
            while current != None:
                if el == current.data:
                    if current.right != None:
                        if current.right.left != None:
                            cur = current.right
                            pre: Node = None
                            while cur.left != None:
                                pre = cur
                                cur = cur.left
                            cur.left = current.left
                            cur.right = current.right
                            if prev == None:
                                self.__head == cur
                                pre.left = None
                                return True
                            if path == "Right":
                                prev.right = cur
                            elif path == "Left":
                                prev.left = cur
                            pre.left = None
                        elif current.right.left == None:
                            current.right.left = current.left
                            if path == "Right":
                                prev.right = current.right
                            elif path == "Left":
                                prev.left = current.right
                    elif current.right == None:
                        if current.left != None:
                            if path == "Right":
                                prev.right = current.left
                            elif path == "Left":
                                prev.left = current.left
                        elif current.left == None:
                            if path == "Right":
                                prev.right = None
                            elif path == "Left":
                                prev.left = None
                    return True
                elif el > current.data:
                    prev = current
                    current = current.right
                    path = "Right"
                elif el < current.data:
                    prev = current
                    current = current.left
                    path = "Left"
            return False

    def in_order(self):
        self.__InOrder(self.__head)

    def __InOrder(self, current: Node):
        if current == None:
            return
        self.__InOrder(current.left)
        print(current.data, end=" | ")
        self.__InOrder(current.right)

    def pre_order(self):
        self.__PreOrder(self.__head)

    def __PreOrder(self, current: Node):
        if current == None:
            return
        print(current.data, end=" | ")
        self.__PreOrder(current.left)
        self.__PreOrder(current.right)

    def post_order(self):
        self.__PostOrder(self.__head)

    def __PostOrder(self, current: Node):
        if current == None:
            return
        self.__PostOrder(current.left)
        self.__PostOrder(current.right)
        print(current.data, end=" | ")
