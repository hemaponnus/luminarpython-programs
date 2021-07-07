
## 19/3/21-18


class Employee:
    cpy_name = "paragon"
    def __init__(self, id, name, age,salary ):
        self.id = id
        self.name = name
        self.age = age
        self.salary=salary
    def print(self):
        print("id", self.id)
        print("name", self.name)
        print("age", self.age)
        print("cpy name", Employee.cpy_name)
        print("salary",self.salary)


obj = Employee(123, "asdff", 24,23000)
obj.print()
                        # output

                  #id 123
                  #name asdff
                  #age 24
                  #cpy name paragon
                  #salary 23000
