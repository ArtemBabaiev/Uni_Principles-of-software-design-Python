class ValError(Exception):
    pass
class FormatError(Exception):
    pass

class Time():
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        if isinstance(hours, int):
            if hours < 24 and hours >= 0:
                self.__hours = hours
            else:
                raise FormatError("Не правильний формат часу")
        else:
            raise ValError("Повинно бути int")
        if isinstance(minutes, int):
            if minutes < 60 and minutes >= 0:
                self.__minutes = minutes
            else:
                raise FormatError("Не правильний формат часу")
        else:
            raise ValError("Повинно бути int")
        if isinstance(seconds, int):
            if seconds < 60 and seconds >= 0:
                self.__seconds = seconds
            else:
                raise FormatError("Не правильний формат часу")
        else:
            raise ValError("Повинно бути int")
    
    @property
    def Hours(self):
        return self.__hours

    @Hours.setter
    def Hours(self, value):
        if isinstance(value, int):
            if value < 24 and value >= 0:
                self.__hours = value
            else:
                raise FormatError("Не правильний формат часу")
        else:
            raise ValError("Повинно бути int")
    
    @property
    def Minutes(self):
        return self.__minutes

    @Minutes.setter
    def Minutes(self, value):
        if isinstance(value, int):
            if value < 60 and value >= 0:
                self.__minutes = value
            else:
                raise FormatError("Не правильний формат часу")
        else:
            raise ValError("Повинно бути int")
   
    @property
    def Seconds(self):
        return self.__seconds

    @Seconds.setter
    def Seconds(self, value):
        if isinstance(value, int):
            if value < 60 and value >= 0:
                self.__seconds = value
            else:
                raise FormatError("Не правильний формат часу")
        else:
            raise ValError("Повинно бути int")
    
    def ChangeHours(self, change):
        if isinstance(change, int):
            if self.__hours + change%24 > 23:
                self.__hours = self.__hours + change%24 - 24
            else:
                self.__hours += change % 24
        else:
            raise ValError("Повинно бути int")
    
    def ChangeMinutes(self, change):
        if isinstance(change, int):
            perenos = change//60
            if self.__minutes + (change%60)>59:
                if change>0:
                    perenos+=1
                    self.__minutes = self.__minutes + change%60 - 60
                else:
                    perenos-=1
                    self.__minutes = abs(abs(self.__minutes - change%60) - 60)
            else:
                self.__minutes+=change % 60
            if perenos != 0:
                self.ChangeHours(perenos)
        else:
            raise ValError("Повинно бути int")
    
    def ChangeSeconds(self, change):
        if isinstance(change, int):
            perenos = change//60
            if self.__seconds + (change%60)>59:
                if change>0:
                    perenos+=1
                    self.__seconds = self.__seconds + change%60 - 60
                else:
                    perenos-=1
                    self.__seconds = abs(abs(self.__seconds - change%60) - 60)
            else:
                self.__seconds+=change % 60
            if perenos != 0:
                self.ChangeMinutes(perenos)
        else:
            raise ValError("Повинно бути int")
    
    def PrintTime(self):
        print("%s:%s:%s" % (self.__hours, self.__minutes, self.__seconds))
    
    @property
    def GetTime(self):
        return [self.__hours, self.__minutes, self.__seconds]
    
if True:
    sec = int(input("Введіть секунди: "))
    minu = int(input("Введіть хвилини: "))
    hou = int(input("Введіть години: "))
    time = Time(hou, minu, sec)
    repit = "no"
    while repit!="exit":
        time.ChangeSeconds(int(input("Зміна секунд на: ")))
        time.PrintTime()
        time.ChangeMinutes(int(input("Зміна хвилин на: ")))
        time.PrintTime()
        time.ChangeHours(int(input("Зміна годин на : ")))
        time.PrintTime()
        repit = input("Введіть exit для закінчення: ")
    repit = "no"
    zerotime = Time()
    zerotime.PrintTime()
    while repit!="exit":
        zerotime.Seconds = int(input("Зміна секунд: "))
        zerotime.Minutes = int(input("Зміна хвилин: "))
        zerotime.Hours = int(input("Зміна годин: "))
        repit = input("Введіть exit для закінчення: ")
    arr = zerotime.GetTime
    for el in arr:
        print(str(el), end= " | ")
    print()
