



class Employee(object):

    def __init__(self, eid, ename, desig, salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary

    def print_emp(self):
        print(self.ename)
    def __str__(self):
        return self.ename+self.desig+str(self.eid)+str(self.salary)


emp=Employee(1000,"varun","developer",25000)
emp1=Employee(1000,"arun","developer",25000)
employees=[]
employees.append(emp)
employees.append(emp1)
devop=list(filter(lambda emp:emp.desig=="developer",employees))
for dev in devop:
    print(dev)
