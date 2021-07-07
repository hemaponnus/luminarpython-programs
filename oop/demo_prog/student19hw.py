class Student:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def printval(self):
        print("name:", self.name)
        print("age:", self.age)

    def __str__(self):
        return self.name

f = open("C:/Users/hemaponnus/PycharmProjects/feb python/oop/demo_prog/student19", "r")
for lines in f:
    data = lines.split(",")
    name = data[0]
    age = data[1]
    obj = Student(name,age)
    print(obj)
    obj.printval()

    ## output ##

    # anu
    # name: anu
    # age: 22

    # rahul
    # name: rahul
    # age: 23

    # vinod
    # name: vinod
    # age: 31

    # ajay
    # name: ajay
    # age: 27

    # maya
    # name: maya
    # age: 26

