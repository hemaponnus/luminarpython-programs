

  # 22/3/21-19

class Employee:
    cpy_name="paragon"
    def __init__(self,name,id,age,salary):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary
    def __int__(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.salary)
        print(Employee.cpy_name)
    def __str__(self):
        return str(self.id)
emp=Employee("hema",123,23,12000)
print(emp)