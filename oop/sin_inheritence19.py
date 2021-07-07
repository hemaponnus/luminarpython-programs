
  #22/3/21-19

                        ##   inherie + constructo

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print(self.rollno)
        print(self.mark)
obj=Student(1,34,"jithus",22)
obj.print()
obj.printval()


                  ## output

        #1
        #34
        #name jithus
        #age 22
