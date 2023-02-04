class Car():
    def __init__(self, name:str = "default", maxSpeed:int =-1, color:str = "default"):
        
        self._name = name
        self._maxSpeed = maxSpeed
        self._color = color
    def Cost(self):
        return self._maxSpeed*100
    def UpdateOfModel(self):
        self._maxSpeed +=10
    def Information(self):
        print("Назва: {name} | Максимальна швидкість: {maxSpeed} | Колір: {color} | Вартість: {price}".format(name=self._name, maxSpeed=self._maxSpeed, color=self._color, price=self.Cost()))
class SportCar(Car):
    def __init__(self, name:str = "default", maxSpeed:int =-1, color:str = "default", numOfSeats = -1):
        Car.__init__(self, name, maxSpeed, color)
        self.__numOfSeats = numOfSeats
    def Cost(self):
        return self._maxSpeed * 350
    def UpdateOfModel(self):
        self._maxSpeed += 100
    def Information(self):
        Car.Information(self)
        print("Кіль-сть місць: {seats}".format(seats=self.__numOfSeats))
class ExcutiveCar(Car):
    def __init__(self, name:str = "default", maxSpeed:int =-1, color:str = "default", isCond:bool = False):
        Car.__init__(self, name, maxSpeed, color)
        self.__isCond = isCond
    def Cost(self):
        return self._maxSpeed *250
    def UpdateOfModel(self):
        self._maxSpeed += 50
    def Information(self):
        Car.Information(self)
        print("Наявність кондиціонеру: {Cond}".format(Cond=self.__isCond))

if True:
    car= Car("Ford", 220, "red")
    sportcar = SportCar("Porsche" , 280, "green", 4)
    execCar= ExcutiveCar("BMW", 220, "black", True)
    print("Car".center(25, "*"))
    car.Information()
    print("SportCar".center(25, "*"))
    sportcar.Information()
    print("ExecCar".center(25, "*"))
    execCar.Information()
    car.UpdateOfModel()
    sportcar.UpdateOfModel()
    execCar.UpdateOfModel()
    print("Car".center(25, "*"))
    car.Information()
    print("SportCar".center(25, "*"))
    sportcar.Information()
    print("ExecCar".center(25, "*"))
    execCar.Information()
    