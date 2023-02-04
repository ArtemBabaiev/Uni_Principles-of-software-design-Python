import re
class ValError(Exception):
    pass
class IndxError(Exception):
    pass

class Point:
    def __init__(self,  x = 0, y = 0, color = "black" ):
        if isinstance(x, float) or isinstance(x, int):
            self.__x = x
        else:
            raise ValError("Некоректний тип")
        if isinstance(y, float) or isinstance(y, int):
            self.__y = y
        else:
            raise ValError("Некоректний тип")
        self.__color = color
        self.__data = [self.__x, self.__y, self.__color]
    
    def __getitem__(self, index):
        return self.__data[index]
    
    def __setitem__(self, index, value):
        try:
            self.__data[index] = value
        except IndexError:
            raise IndexError("Incorrect index")
        else:
            if index == 0:
                if isinstance(value, float) or isinstance(value, int):
                    self.__x = value
                else:
                    raise ValError("Некоректний тип")
            elif index == 1:
                if isinstance(value, float) or isinstance(value, int):
                    self.__y = value
                else:
                    raise ValError("Некоректний тип")
            elif index == 2:
                if isinstance(value, str) or isinstance(value, str):
                    self.__color = value
                else:
                    raise ValError("Некоректний тип")
            
    def __iadd__(self, value):
        if isinstance(value, float) or isinstance(value, int):  
            self.__x+=value
            self.__y+=value
            return self
        else:
            raise ValError("Некоректний тип")
    
    def __isub__(self, value):
        if isinstance(value, float) or isinstance(value, int):  
            self.__x-=value
            self.__y-=value
            return self
        else:
            raise ValError("Некоректний тип")
    
    def __bool__(self):
        if self.__x == self.__y:
            return True
        else:
            return False

    def __add__(self, value):
        if isinstance(value, float) or isinstance(value, int):  
            self.__x+=value
            self.__y+=value
            return self
        else:
            raise ValError("Некоректний тип")
    
    def __str__(self):
        return "%s %s %s" % (self.__x, self.__y, self.__color)
    
    @staticmethod
    def toPoint( string):
        arr = re.split(r"[ ]", string)
        return Point(int(arr[0]), int(arr[1]), arr[2])

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







if True:
    point = Point(1, 1, "blue")
    point[0] = 5
    print(point[0])
    point.print_coordinates()
    if point:
        print("true 1")
    else:
        print("false 1")
    point[1] = 5
    if point:
        print("true 2")
    else:
        print("false 2")
    point+=1
    point.print_coordinates()
    point+1
    point.print_coordinates()
    print(str(point))
    converted_point = Point.toPoint("4 5 red")
    print("***************************************************************************************************************")
    converted_point.print_coordinates()
    print(converted_point.Color)
    # zeropoint = Point("red")
    # print("Початкові координати")
    # point.print_coordinates()
    # print("Координати точки після переміщення: ")
    # point.move(4, -3)
    # point.print_coordinates()
    # print("Колір точки: %s" % point.Color)
    # point.X = 5
    # print("Координата X: %s" % point.X)