
## 19/3/21-18

class Employee:
    cpy_name="paragon"
    def detail(self,id,name,age,):
        self.id=id
        self.name=name
        self.age=age
    def print(self):
        print("id",self.id)
        print("name",self.name)
        print("age",self.age)
        print("cpy name",Employee.cpy_name)
obj=Employee()
obj.detail(123,"asdff",24)
obj.print()
obj1=Employee()
                                   ## output ##
                                #id 123
                                #name asdff
                                #age 24
                                #cpy name paragon
