class Person():
    def __init__(self, name:str = "default name", sex:str = "default sex", age:int = -1):
        self.__name = name
        self.__sex = sex
        self.__age = age
    def __del__(self):
        print("Персону видалено")
    def Show(self):
        print("Ім'я: {name}; Стать: {sex}; Вік: {age}".format(name=self.__name, sex=self.__sex, age=self.__age))
    def Activity(self):
        print("прокинутися, поїсти, піти на роботу, попрацювати, прийти додому, поїсти, спати")
class Student(Person):
    def __init__(self, name:str = "default name", sex:str = "default sex", age:int = -1, \
        yearOfStudy:int = -1, averageMark:float = -1.0, formOfEducation:str = "default"):
        Person.__init__(self, name = name, sex = sex, age = age)
        self.__yearOfStudy = yearOfStudy
        self.__averageMark = averageMark
        self.__formOfEducation = formOfEducation
    def __del__(self):
        print("Студента видалено")
    def Show(self):
        Person.Show(self)
        print("Курс: {yearOfStudy} | Середній бал: {averageMark} | Форма навчання: {formOfEducation}".format(yearOfStudy=self.__yearOfStudy, averageMark = self.__averageMark, formOfEducation=self.__formOfEducation))
    def Activity(self):
        print("Прокинутися, піти на пару, попрацювати на парі, поїсти підчас пари, піти спати")

class Teacher(Person):
    def __init__(self, name:str = "default name", sex:str = "default sex", age:int = -1, \
        disciplines:str = "default", salary:int = -1, experience:int = -1):
        Person.__init__(self, name = name, sex = sex, age = age)
        self.__disciplines = disciplines
        self.__salary = salary
        self.__experience = experience
    def __del__(self):
        print("Викладча видалено")
    def Show(self):
        Person.Show(self)
        print("Дисципліни: {disciplines} | Стаж: {experience} | Зарплатня: {salary}".format(disciplines=self.__disciplines,experience=self.__experience, salary=self.__salary))
    def Activity(self):
        print("Викладає")
class Head(Person):
    def __init__(self, name:str = "default name", sex:str = "default sex", age:int = -1, \
        cathedra:str = "default", yearsAsHead:int = -1, salary:int = -1):
        Person.__init__(self, name = name, sex = sex, age = age)
        self.__cathedra = cathedra
        self.__yearsAsHead = yearsAsHead
        self.__salary = salary
    def __del__(self):
        print("Зав.кафедри видалено")
    def Show(self):
        Person.Show(self)
        print("Кафедра: {cathedra} | Років на посаді: {yearsAsHead} | Зарплата: {salary}".format(cathedra = self.__cathedra, yearsAsHead = self.__yearsAsHead, salary = self.__salary))
    def Activity(self):
        print('Завідує')

if True:
    person = Person()
    student = Student("art", "male", 18, 1, 1.0, "D")
    teacher = Teacher()
    head = Head()
    
    person.Show()
    print(125*"*")
    student.Show()
    print(125*"*")
    teacher.Show()
    print(125*"*")
    head.Show()
    print(125*"*")

    person.Activity()
    student.Activity()
    teacher.Activity()
    head.Activity()

