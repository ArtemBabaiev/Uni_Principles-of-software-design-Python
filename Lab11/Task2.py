from Exceptions import *
class VectorInt:
    __numVec = 0
    def __init__(self, size = 1, toFill = 0):
        if isinstance(size, int) and isinstance(toFill, int):
            if size >= 0:
                self.__size = size
                self.__IntArray = [toFill for i in range(size)]
            else: raise Size_Error(''''Повинно бути не від'ємним''')
        else:
            raise Type_Error("Повинно бути int") 
        self.__codeError = None
        self.__class__.__numVec +=1
        
    def __del__(self):
        self.__class__.__numVec -=1
        print('Ветктор видалено')
    
    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= 0 and index < self.__size:
                return self.__IntArray[index]
            else:
                self.CodeError = -1
                return 0
            
        else:
            raise Type_Error('Повинно бути int')        
    def __setitem__(self, index, value):
        if isinstance(value, int):
            if isinstance(index, int):
                if index >= 0 and index < self.__size:
                    self.__IntArray[index] = value
                else:
                    self.CodeError = -1
            else:
                raise Type_Error('Індекс повинен бути int')
        else:
            raise Type_Error('Значення повинно бути int')

    def set_elements(self):
        for i in range(self.__size):
            self[i] = int(input("Введыть %s елемент: " % i))
    
    def print_vector(self):
        for el in self.__IntArray:
            print(str(el).ljust(4), end="| ")
        print()

    def set_with_vector(self, arr):
        if isinstance(arr, list):
            for el in arr:
                if not isinstance(el, int):
                    raise Type_Error("В масиві міститься не int значення")
        self.__IntArray = arr.copy()
        self._size = len(arr)
    
    @staticmethod
    def get_num():
        return __class__.__numVec
    
    def set_with_param(self, param):
        if isinstance(param, int):
            for i in range(self.Size):
                self[i] = param
        else:
            raise Type_Error("Повинно бути int")
    
    @property
    def Size(self):
        return self.__size

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
            for i in range(self.Size):
                self[i] += value
            return self
        else:
            raise Type_Error("Повинно бути int")
    def __isub__(self, value):
        if isinstance(value, int):
            for i in range(self.Size):
                self[i] -= value
            return self
        else:
            raise Type_Error("Повинно бути int")

    def __bool__(self):
        if self.Size == 0:
            return False
        else:
            for i in range(self.Size):
                if self[i] == 0:
                    return False
            return True
    def __invert__(self):
        toReturn = VectorInt(self.Size)
        for i in range(self.Size):
            toReturn[i] = ~self.__IntArray[i]
        return toReturn
    
    def __add__(self, other):
        if isinstance(other, VectorInt):
            if self.Size >= other.Size:
                toReturn = VectorInt(self.Size)
                for i in range(self.Size):
                    if i < other.Size:
                        toReturn[i] = self[i] + other[i]
                    else:
                        toReturn[i] = self[i]
                return toReturn
            else:
                toReturn = VectorInt(other.Size)
                for i in range(other.Size):
                    if i < self.Size:
                        toReturn[i] = self[i] + other[i]
                    else:
                        toReturn[i] = other[i]
                return toReturn
        elif isinstance(other, int):
            toReturn = VectorInt(self.Size)
            for i in range(self.Size):
                toReturn[i]=self[i] + other
            return toReturn
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __sub__(self, other):
        if isinstance(other, VectorInt):
            if self.Size >= other.Size:
                toReturn = VectorInt(self.Size)
                for i in range(self.Size):
                    if i < other.Size:
                        toReturn[i] = self[i] - other[i]
                    else:
                        toReturn[i] = self[i]
                return toReturn
            else:
                toReturn = VectorInt(other.Size)
                for i in range(other.Size):
                    if i < self.Size:
                        toReturn[i] = self[i] - other[i]
                    else:
                        toReturn[i] = other[i]
                return toReturn
        elif isinstance(other, int):
            toReturn = VectorInt(self.Size)
            for i in range(self.Size):
                toReturn[i]=self[i] - other
            return toReturn
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __mul__(self, other):
        if isinstance(other, VectorInt):
            if self.Size >= other.Size:
                toReturn = VectorInt(self.Size)
                for i in range(self.Size):
                    if i < other.Size:
                        toReturn[i] = self[i] * other[i]
                    else:
                        toReturn[i] = self[i]
                return toReturn
            else:
                toReturn = VectorInt(other.Size)
                for i in range(other.Size):
                    if i < self.Size:
                        toReturn[i] = self[i] * other[i]
                    else:
                        toReturn[i] = other[i]
                return toReturn
        elif isinstance(other, int):
            toReturn = VectorInt(self.Size)
            for i in range(self.Size):
                toReturn[i]=self[i] * other
            return toReturn
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __truediv__(self, other):
        if isinstance(other, VectorInt):
            if self.Size >= other.Size:
                toReturn = VectorInt(self.Size)
                for i in range(self.Size):
                    if i < other.Size:
                        toReturn[i] = self[i] / other[i]
                    else:
                        toReturn[i] = self[i]
                return toReturn
            else:
                toReturn = VectorInt(other.Size)
                for i in range(other.Size):
                    if i < self.Size:
                        toReturn[i] = self[i] / other[i]
                    else:
                        toReturn[i] = other[i]
                return toReturn
        elif isinstance(other, int):
            toReturn = VectorInt(self.Size)
            for i in range(self.Size):
                toReturn[i]= int(self[i] / other)
            return toReturn
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __mod__(self, other):
        if isinstance(other, VectorInt):
            if self.Size >= other.Size:
                toReturn = VectorInt(self.Size)
                for i in range(self.Size):
                    if i < other.Size:
                        toReturn[i] = self[i] % other[i]
                    else:
                        toReturn[i] = self[i]
                return toReturn
            else:
                toReturn = VectorInt(other.Size)
                for i in range(other.Size):
                    if i < self.Size:
                        toReturn[i] = self[i] % other[i]
                    else:
                        toReturn[i] = other[i]
                return toReturn
        elif isinstance(other, int):
            toReturn = VectorInt(self.Size)
            for i in range(self.Size):
                toReturn[i]=self[i] % other
            return toReturn
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __or__(self, other):
        if isinstance(other, VectorInt):
            if self.Size >= other.Size:
                toReturn = VectorInt(self.Size)
                for i in range(self.Size):
                    if i < other.Size:
                        toReturn[i] = self[i] | other[i]
                    else:
                        toReturn[i] = self[i]
                return toReturn
            else:
                toReturn = VectorInt(other.Size)
                for i in range(other.Size):
                    if i < self.Size:
                        toReturn[i] = self[i] | other[i]
                    else:
                        toReturn[i] = other[i]
                return toReturn
        elif isinstance(other, int):
            toReturn = VectorInt(self.Size)
            for i in range(self.Size):
                toReturn[i]=self[i] | other
            return toReturn
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __and__(self, other):
        if isinstance(other, VectorInt):
            if self.Size >= other.Size:
                toReturn = VectorInt(self.Size)
                for i in range(self.Size):
                    if i < other.Size:
                        toReturn[i] = self[i] & other[i]
                    else:
                        toReturn[i] = self[i]
                return toReturn
            else:
                toReturn = VectorInt(other.Size)
                for i in range(other.Size):
                    if i < self.Size:
                        toReturn[i] = self[i] & other[i]
                    else:
                        toReturn[i] = other[i]
                return toReturn
        elif isinstance(other, int):
            toReturn = VectorInt(self.Size)
            for i in range(self.Size):
                toReturn[i]=self[i] & other
            return toReturn
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __xor__(self, other):
        if isinstance(other, VectorInt):
            if self.Size >= other.Size:
                toReturn = VectorInt(self.Size)
                for i in range(self.Size):
                    if i < other.Size:
                        toReturn[i] = self[i] ^ other[i]
                    else:
                        toReturn[i] = self[i]
                return toReturn
            else:
                toReturn = VectorInt(other.Size)
                for i in range(other.Size):
                    if i < self.Size:
                        toReturn[i] = self[i] ^ other[i]
                    else:
                        toReturn[i] = other[i]
                return toReturn
        elif isinstance(other, int):
            toReturn = VectorInt(self.Size)
            for i in range(self.Size):
                toReturn[i]=self[i] ^ other
            return toReturn
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __lshift__(self, other):
        if isinstance(other, int):
            for i in range(self.Size):
                self[i] <<= other
            return self
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __rshift__(self, other):
        if isinstance(other, int):
            for i in range(self.Size):
                self[i] >>= other
            return self
        else:
            raise Type_Error("Операція неможлива з цим типом")

    def __eq__(self, other):
        if isinstance(other, VectorInt):
            if self.Size != other.Size:
                return False
            else:
                for i in range(self.Size):
                    if (self[i] != other[i]):
                        return False
                return True
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __ne__(self, other):
        if isinstance(other, VectorInt):
            if self.Size != other.Size:
                return True
            else:
                for i in range(self.Size):
                    if (self[i] != other[i]):
                        return True
                return False
        else:
            raise Type_Error("Операція неможлива з цим типом")
    
    def __gt__(self, other):
        if isinstance(other, VectorInt):
            if self.Size != other.Size:
                return False
            else:
                for i in range(self.Size):
                    if self[i]<=other[i]:
                        return False
                return True
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __lt__(self, other):
        if isinstance(other, VectorInt):
            if self.Size != other.Size:
                return False
            else:
                for i in range(self.Size):
                    if self[i]>=other[i]:
                        return False
                return True
        else:
            raise Type_Error("Операція неможлива з цим типом")
            
    def __le__(self, other):
        if isinstance(other, VectorInt):
            if self.Size != other.Size:
                return False
            else:
                for i in range(self.Size):
                    if self[i]>other[i]:
                        return False
                return True
        else:
            raise Type_Error("Операція неможлива з цим типом")
    def __ge__(self, other):
        if isinstance(other, VectorInt):
            if self.Size != other.Size:
                return False
            else:
                for i in range(self.Size):
                    if self[i]<other[i]:
                        return False
                return True
        else:
            raise Type_Error("Операція неможлива з цим типом")

if True:
    vec1 = VectorInt(5)
    vec2 = VectorInt(4, 3)
    vec1.print_vector()
    vec2.print_vector()
    print("Поелементне перезадання вектора")
    vec2.set_elements()
    vec2.print_vector()
    print("Зміна значень вектора скаляром 9")
    vec1.set_with_param(9)
    vec1.print_vector()
    print("Перезадання вектора вектором")
    vec1.set_with_vector([1, 8, 9, 5, 2])
    vec1.print_vector()
    print("Кількість створених векторів %s" % VectorInt.get_num())
    print("Довжина вектора 1:%s. Довжина вектора 2:%s" % (vec1.Size, vec2.Size))
    vec1.CodeError = 0
    print("Індексатор %s" % vec1[500])
    print("Помислка %s" % vec1.CodeError)
    
    print("Початкові вектори")
    vec1.print_vector()
    vec2.print_vector()
    print("Перевірка += та -=")
    vec1+=1
    vec2-=1
    vec1.print_vector()
    vec2.print_vector()

    print("Перевірка true, false")
    if vec1:
        print("True 1")
    else:
        print("False 1")

    print("Перевірка ~")
    print(~vec1)
    print()
    print("\n Перевірка ариф. операцій")
    print("Перевірка +")
    res = vec1+vec2
    res.print_vector()
    res = res +2
    res.print_vector()

    print("Перевірка -")
    res = vec1-vec2
    res.print_vector()
    res = res - 2
    res.print_vector()
    print("Перевірка *")
    res = vec1*vec2
    res.print_vector()
    res = res * 2
    res.print_vector()
    print("Перевірка /")
    res = vec1-vec2
    res.print_vector()
    res = res / 2
    res.print_vector()
    print("Перевірка %")
    res = vec1-vec2
    res.print_vector()
    res = res % 2
    res.print_vector()

    print("Перевірка |")
    res = vec1-vec2
    res.print_vector()
    res = res | 2
    res.print_vector()

    print("Перевірка &")
    res = vec1-vec2
    res.print_vector()
    res = res & 2
    res.print_vector()

    print("Перевірка ^")
    res = vec1-vec2
    res.print_vector()
    res = res ^ 2
    res.print_vector()

    print("Перевірка >>")
    res = vec1 >>2
    res.print_vector()
    print("Перевірка <<")
    res = vec1 <<2
    res.print_vector()

    print("Перевірка порівнянь")
    if (vec1 == vec2):
        print("== true")
    else:
        print("== false")
    if (vec1 != vec2):
        print("!= true")
    else:
        print("!= false")
    if (vec1 > vec2):
        print("> true")
    else:
        print("> false")
    if (vec1 < vec2):
        print("< true")
    else:
        print("< false")
    if (vec1 >= vec2):
        print(">= true")
    else:
        print(">= false")
    if (vec1 <= vec2):
        print("<= true")
    else:
        print("<= false")  