class ValError(Exception):
    pass

class Point:
    def __init__(self, color , x = 0, y = 0 ):
        if isinstance(x, float) or isinstance(x, int):
            self.__x = x
        else:
            raise ValError("Повинно бути число")
        if isinstance(y, float) or isinstance(y, int):
            self.__y = y
        else:
            raise ValError("Повинно бути число")
        self.__color = color
    def print_coordinates(self):
        print("Координатa X: %s\nКоординатa Y: %s" % (self.__x, self.__y))
    def eval_len(self):
        return (self.__x**2 + self.__y**2)**0.5
    def move(self, a, b):
        if isinstance(a, float) or isinstance(a, int):
            self.__x += a
        else:
            raise ValError("Повинно бути число")
        if isinstance(b, float) or isinstance(b, int):
            self.__y += b
        else:
            raise ValError("Повинно бути число")
    @property
    def X(self):
        return self.__x
    @X.setter
    def X(self, value):
        self.__x = value
    @property
    def Y(self):
        return self.__y
    @Y.setter
    def Y(self, value):
        self.__y = value
    @property
    def Color(self):
        return self.__color
if True:
    point = Point("blue", 1, 1)
    zeropoint = Point("red")
    print("Початкові координати")
    point.print_coordinates()
    print("Координати точки після переміщення: ")
    point.move(4, -3)
    point.print_coordinates()
    print("Колір точки: %s" % point.Color)
    point.X = 5
    print("Координата X: %s" % point.X)