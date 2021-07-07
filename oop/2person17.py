
# 18/3/21-17


#class Person:
#    def setval(self,name,age):
#        self.age=age
#        self.name=name
#    def printvalue(self):
#        print("name",self.name)
#        print("age",self.age)
#obj=Person()
#obj.setval("arun",25)
#obj.printvalue()

                          ## output

                      #   name arun
                      #   age 25


class Employee:
    def setval(self,id,name,age,salary,exp):
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary
        self.exp=exp
    def printval(self):
        print("id",self.id)
        print("name",self.name)
        print("age",self.age)
        print("salary",self.salary)
        print("experience",self.exp)
enp=Employee()
enp.setval(123,"hema",23,12000,5)
enp.printval()

                             ## output
                          #   id 123
                          #name hema
                          #age 23
                          #salary 12000
                          #experience 5