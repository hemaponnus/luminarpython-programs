
   ## 19/3/21-18

class E1:
    def __init__(self,id,name,age,salary):
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary
    def m1(self):
        print("e1-class",self.id)
        print("e1-class",self.name)
        print("e1-class",self.age)
        print("e1-class",self.salary)
class E2(E1):
      def m2(self,id,name,age,salary):
          self.id = id
          self.name = name
          self.age = age
          self.salary = salary
      def m3(self):
          print("e2-class",self.id)
          print("e2-class",self.name)
          print("e2-class",self.age)
          print("e2-class",self.salary)
class E3(E2):
    def m4(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def m5(self):
        print("e3-class",self.id)
        print("e3-class",self.name)
        print("e3-class",self.age)
        print("e3-class",self.salary)

obj=E3(1111,"ponnu",23,14000)
obj.m1()
obj.m4(4444,"hema",22,12000)
obj.m5()
obj.m2(3333,"Amal",22,13000)
obj.m3()

                                    ## output

                          #e1-class 1111
                          #e1-class ponnu
                          #e1-class 23
                          #e1-class 14000
                          #e3-class 4444
                          #e3-class hema
                          #e3-class 22
                          #e3-class 12000
                          #e2-class 3333
                          #e2-class Amal
                          #e2-class 22
                          #e2-class 13000

