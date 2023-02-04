class Computer():
    def __init__(self, processor, frequency, gpu, videoMemory, ram, frequencyOfRam, isGoodCoolSystem):
        self.__processor = processor
        self.__frequency = frequency
        self.__gpu = gpu
        self.__videoMemory = videoMemory
        self.__ram = ram
        self.__frequencyOfRam = frequencyOfRam
        self.__isGoodCoolSystem = isGoodCoolSystem
    def boostCPU(self, increase):
        if self.__isGoodCoolSystem:
            self.__frequency += increase
            return "Процессор розігнано до частоти %s" % self.__frequency
        else:
            return "Система охолодження погана. Розгін не рекомендується"
    def ChangeVideoCard(self, newType, capacity):
        self.__gpu = newType
        self.__videoMemory = capacity
        return "Виконано заміну відеокарти на %s з об\'ємом відеопам\'яті %s" % (self.__gpu, self.__videoMemory)
    def CompatibilityOfRAM(self, newRAMFreq, newRAMCap):
        good = True
        if (newRAMFreq != self.__frequencyOfRam):
            good = False
        if (newRAMCap != self.__ram):
            good = False
        return good
    def PrintChar(self):
        print("CPU: %s | CPU freq: %s | GPU: %s | Video Memory: %s | RAM: %s | Freq RAM: %s | IsCoolSystem: %s" %\
             (self.__processor, self.__frequency, self.__gpu, self.__videoMemory, self.__ram, self.__frequencyOfRam, self.__isGoodCoolSystem))

if True:
    proc = input("Введіть CPU: ")
    procFreq = int(input("Його частоту: "))
    video = input("Введіть GPU: ")
    Vmem = int(input("Її вміст відео пам'яті: "))
    ram = int(input("Кіль-сть ОП: "))
    ramfreq = int(input("Її частота: "))
    coolsyst = bool(input("Чи добра сист. охолдження True/eps: "))
    comp = Computer(proc, procFreq, video, Vmem, ram, ramfreq, coolsyst)
    comp.PrintChar()
    print(comp.boostCPU(25))
    print(comp.ChangeVideoCard("560r", 2))
    if (comp.CompatibilityOfRAM(4500, 8)):
        print("Додавання можливе")
    else:
        print("Додавання не рекомендується")
    comp.PrintChar()