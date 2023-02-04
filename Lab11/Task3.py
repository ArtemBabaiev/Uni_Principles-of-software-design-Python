from Task2 import VectorInt
from Exceptions import *
class MatrixInt():
    __num_m = 0
    def __init__(self, n:int=0, m:int= 0, toFill:int= 0):
        if isinstance(n, int) and isinstance(m, int) and isinstance(toFill, int):
            self.__n = n
            self.__m = m
            self.__IntArray = [[toFill for j in range(m)] for i in range(n)]
            self.__class__.__num_m += 1
            self.__codeError = None
        else:
            raise Type_Error("Повинно бути int")
    def __del__(self):
        self.__class__.__num_m -=1
        print('Матрицю видалено')
    def __getitem__(self, index):
        if len(index) == 1:
            if isinstance(index[0], int):
                i = index//self.Size[0]
                j = index%self.Size[0]
                if i < self.Size[0] and i >= 0 and j >= 0 and j < self.Size[1]:
                    return self.__IntArray[i][j]
                else:
                    self.__codeError = -1
                    return 0
            else:
               raise Type_Error("Повинно бути int") 
        elif len(index) == 2:
            if isinstance(index[0], int) and isinstance(index[1], int):
                if index[0] < self.Size[0] and index[0] >= 0 and index[1] >= 0 and index[1] < self.Size[1]:
                    return self.__IntArray[index[0]][index[1]]
                else:
                    self.__codeError = -1
                    return 0
            else:
               raise Type_Error("Повинно бути int") 
        else:
            raise Arguments_Error("Невірна кількість індексів")
    def __setitem__(self, index, value:int):
        if isinstance(value, int):
            if len(index) == 1:
                if isinstance(index[0], int):
                    i = index//self.Size[0]
                    j = index%self.Size[0]
                    if i < self.Size[0] and i >= 0 and j >= 0 and j < self.Size[1]:
                        self.__IntArray[i][j] = value
                    else:
                        self.__codeError = -1
                else:
                    raise Type_Error("Індекс повинен бути int") 
            elif len(index) == 2:
                if isinstance(index[0], int) and isinstance(index[1], int):
                    if index[0] < self.Size[0] and index[0] >= 0 and index[1] >= 0 and index[1] < self.Size[1]:
                        self.__IntArray[index[0]][index[1]] = value
                    else:
                        self.__codeError = -1
                else:
                    raise Type_Error("Повинно бути int") 
        else:
            raise Type_Error("Значення бути int") 

    @property
    def Size(self):
        return [self.__n, self.__m]

    def setElements(self):
        for i in range(self.Size[0]):
            for j in range(self.Size[1]):
                self[i,j] = int(input("Введіть ({0};{1}): ".format(i, j)))
    def printMatrix(self):
        for i in range(self.Size[0]):
            for j in range(self.Size[1]):
                print(str(self[i, j]).ljust(4), end="| ")
            print()

    @staticmethod
    def Quantity():
        return __class__.__num_m
    
    def setWithParametr(self, param:int):
        if isinstance(param, int):
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    self[i, j] = param
        else:
            raise Type_Error("Повинно бути int")

    @property
    def CodeError(self):
        return self.__codeError
    @CodeError.setter
    def CodeError(self, value):
        if isinstance(value, int):
            self.__codeError = value
        else:
            raise Type_Error("Повинно бути int")
    
    def __iadd__(self, value):
        if isinstance(value, int):
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    self[i, j] += value
            return self
        else:
            raise Type_Error("Повинно бути int")
    def __isub__(self, value):
        if isinstance(value, int):
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    self[i, j] -= value
            return self
        else:
            raise Type_Error("Повинно бути int")

    def __bool__(self):
        if self.Size[0] == 0 or self.Size[0] == 0:
            return False
        else:
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    if self[i, j] == 0:
                        return False
            return True
    def __invert__(self):
        toReturn = [[0 for i in range(self.Size[1])] for j in range(self.Size[1])]
        for i in range(self.Size[0]):
            for j in range(self.Size[1]):
                toReturn[i][j] = ~self[i,j]
        return toReturn
    
    def __add__(self, value):
        if isinstance(value, int):
            toReturn = MatrixInt(self.Size[0], self.Size[1])
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    toReturn[i,j] = self[i,j] + value
            return toReturn
        elif isinstance(value, MatrixInt):
            if self.Size[0] == value.Size[0] and self.Size[1] == value.Size[1]:
                toReturn = MatrixInt(self.Size[0], self.Size[0])
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        toReturn[i,j] = self[i,j] + value[i,j]
                return toReturn
            else:
                return self
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __sub__(self, value):
        if isinstance(value, int):
            toReturn = MatrixInt(self.Size[0], self.Size[1])
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    toReturn[i,j] = self[i,j] - value
            return toReturn
        if isinstance(value, MatrixInt):
            if self.Size[0] == value.Size[0] and self.Size[1] == value.Size[1]:
                toReturn = MatrixInt(self.Size[0], self.Size[0])
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        toReturn[i,j] = self[i,j] - value[i,j]
                return toReturn
            else:
                return self
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __mul__(self, value):
        if isinstance(value, int):
            toReturn = MatrixInt(self.Size[0], self.Size[1])
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    toReturn[i,j] = self[i,j] * value
            return toReturn
        elif isinstance(value, MatrixInt):
            if self.Size[1] == value.Size[0]:
                toReturn = MatrixInt(self.Size[0], value.Size[1])
                for i in range(self.Size[0]):
                    for j in range(value.Size[1]):
                        for k in range(value.Size[0]):
                            toReturn[i, j] += self[i, k]*value[k, j]
                return toReturn
            else:
                return self
        elif isinstance(value, VectorInt):
            if self.Size[1] == value.Size:
                toReturn = MatrixInt(self.Size[0], 1)
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        toReturn[i, 0] += self[i, j] * self[j]
                return toReturn
            else:
                return self
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __truediv__(self, value):
        if isinstance(value, int):
            toReturn = MatrixInt(self.Size[0], self.Size[1])
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    toReturn[i,j] = int(self[i,j] / value)
            return toReturn
        if isinstance(value, MatrixInt):
            if self.Size[0] == value.Size[0] and self.Size[1] == value.Size[1]:
                toReturn = MatrixInt(self.Size[0], self.Size[0])
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        toReturn[i,j] = int(self[i,j] / value[i,j])
                return toReturn
            else:
                return self
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __mod__(self, value):
        if isinstance(value, int):
            toReturn = MatrixInt(self.Size[0], self.Size[1])
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    toReturn[i,j] = self[i,j] % value
            return toReturn
        elif isinstance(value, MatrixInt):
            if self.Size[0] == value.Size[0] and self.Size[1] == value.Size[1]:
                toReturn = MatrixInt(self.Size[0], self.Size[0])
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        toReturn[i,j] = self[i,j] % value[i,j]
                return toReturn
            else:
                return self
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __or__(self, value):
        if isinstance(value, int):
            toReturn = MatrixInt(self.Size[0], self.Size[1])
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    toReturn[i,j] = self[i,j] | value
            return toReturn
        elif isinstance(value, MatrixInt):
            if self.Size[0] == value.Size[0] and self.Size[1] == value.Size[1]:
                toReturn = MatrixInt(self.Size[0], self.Size[0])
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        toReturn[i,j] = self[i,j] | value[i,j]
                return toReturn
            else:
                return self
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __and__(self, value):
        if isinstance(value, int):
            toReturn = MatrixInt(self.Size[0], self.Size[1])
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    toReturn[i,j] = self[i,j] & value
            return toReturn
        elif isinstance(value, MatrixInt):
            if self.Size[0] == value.Size[0] and self.Size[1] == value.Size[1]:
                toReturn = MatrixInt(self.Size[0], self.Size[0])
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        toReturn[i,j] = self[i,j] & value[i,j]
                return toReturn
            else:
                return self
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __xor__(self, value):
        if isinstance(value, int):
            toReturn = MatrixInt(self.Size[0], self.Size[1])
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    toReturn[i,j] = self[i,j] ^ value
            return toReturn
        elif isinstance(value, MatrixInt):
            if self.Size[0] == value.Size[0] and self.Size[1] == value.Size[1]:
                toReturn = MatrixInt(self.Size[0], self.Size[0])
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        toReturn[i,j] = self[i,j] ^ value[i,j]
                return toReturn
            else:
                return self
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __lshift__(self, value):
        if isinstance(value, int):
            toReturn = MatrixInt(self.Size[0], self.Size[1])
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    toReturn[i, j] = self[i, j] << value
            return toReturn
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __rshift__(self, value):
        if isinstance(value, int):
            toReturn = MatrixInt(self.Size[0], self.Size[1])
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    toReturn[i, j] = self[i, j] >> value
            return toReturn
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __eq__(self, other):
        if isinstance(other, MatrixInt):
            if self.Size[0]==other.Size[0] and self.Size[1]==other.Size[1]:
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        if self[i, j] != other[i, j]:
                            return False
                return True
            else:
                return False
        else:
           raise Type_Error("Операція неможлива з цим типом") 
    def __ne__(self, other):
        if isinstance(other, MatrixInt):
            if self.Size[0]==other.Size[0] and self.Size[1]==other.Size[1]:
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        if self[i, j] != other[i, j]:
                            return True
                return False
            else:
                return True
        else:
           raise Type_Error("Операція неможлива з цим типом") 

    def __gt__(self, other):
        if isinstance(other, MatrixInt):
            if self.Size[0]==other.Size[0] and self.Size[1]==other.Size[1]:
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        if self[i, j] <= other[i, j]:
                            return False
                return True
            else:
                return False
        else:
            raise Type_Error("Операція неможлива з цим типом") 
    def __lt__(self, other):
        if isinstance(other, MatrixInt):
            if self.Size[0]==other.Size[0] and self.Size[1]==other.Size[1]:
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        if self[i, j] >= other[i, j]:
                            return False
                return True
            else:
                return False
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __le__(self, other):
        if isinstance(other, MatrixInt):
            if self.Size[0]==other.Size[0] and self.Size[1]==other.Size[1]:
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        if self[i, j] > other[i, j]:
                            return False
                return True
            else:
                return False
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __ge__(self, other):
        if isinstance(other, MatrixInt):
            if self.Size[0]==other.Size[0] and self.Size[1]==other.Size[1]:
                for i in range(self.Size[0]):
                    for j in range(self.Size[1]):
                        if self[i, j] < other[i, j]:
                            return False
                return True
            else:
                return False
        else:
            raise Type_Error("Операція неможлива з цим типом")



if True:
    mat1 = MatrixInt(3, 3, 2)
    mat2 = MatrixInt(3, 2, 5)
    mat1.printMatrix()
    mat2.printMatrix()
    print("Поелементне перезадання Матриці")
    mat2.setElements()
    mat2.printMatrix()
    print("Зміна значень матриці скаляром 9")
    mat1.setWithParametr(9)
    mat1.printMatrix()
    print("Кількість створених матриц %s" % MatrixInt.Quantity())
    print("Довжина матриці 1:%s. Довжина матриці 2:%s" % (mat1.Size, mat2.Size))
    mat1.CodeError = 0
    print("Індексатор %s" % mat1[1, 2])
    print("Помислка %s" % mat1.CodeError)
    
    print("Початкові вектори")
    mat1.printMatrix()
    mat2.printMatrix()
    print("Перевірка += та -=")
    mat1+=1
    mat2-=1
    mat1.printMatrix()
    mat2.printMatrix()
    
    print("Перевірка true, false")
    if mat1:
        print("True 1")
    else:
        print("False 1")

    print("Перевірка ~")
    print(~mat1)
    print()
    print("\n Перевірка ариф. операцій")
    print("Перевірка +")
    res = mat1+mat2
    res.printMatrix()
    res = res +2
    res.printMatrix()

    print("Перевірка -")
    res = mat1-mat2
    res.printMatrix()
    res = res - 2
    res.printMatrix()
    print("Перевірка *")
    res = mat1*mat2
    res.printMatrix()
    res = res * 2
    res.printMatrix()
    print("Перевірка /")
    res = mat1/mat2
    res.printMatrix()
    res = res / 2
    res.printMatrix()
    print("Перевірка %")
    res = mat1-mat2
    res.printMatrix()
    res = res % 2
    res.printMatrix()

    print("Перевірка |")
    res = mat1-mat2
    res.printMatrix()
    res = res | 2
    res.printMatrix()

    print("Перевірка &")
    res = mat1-mat2
    res.printMatrix()
    res = res & 2
    res.printMatrix()

    print("Перевірка ^")
    res = mat1-mat2
    res.printMatrix()
    res = res ^ 2
    res.printMatrix()

    print("Перевірка >>")
    res = mat1 >>2
    res.printMatrix()
    print("Перевірка <<")
    res = mat1 <<2
    res.printMatrix()

    print("Перевірка порівнянь")
    if (mat1 == mat2):
        print("== true")
    else:
        print("== false")
    if (mat1 != mat2):
        print("!= true")
    else:
        print("!= false")
    if (mat1 > mat2):
        print("> true")
    else:
        print("> false")
    if (mat1 < mat2):
        print("< true")
    else:
        print("< false")
    if (mat1 >= mat2):
        print(">= true")
    else:
        print(">= false")
    if (mat1 <= mat2):
        print("<= true")
    else:
        print("<= false")  