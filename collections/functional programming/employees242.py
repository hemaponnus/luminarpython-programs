class Employee:
    # eid,ename,desig,salary  ## using constructor
    def __init__(self, eid, ename, desig, salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary

    def print_emp(self):
        print(self.ename)
f=open("employees")
employees=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    eid,name,desig,sal=lines.rstrip("\n").split(",")

    e1=Employee(eid,name,desig,sal)

    employees.append(e1)


  ### Employees
#for emp in employees:                                                     # o/p
#    print(emp.eid)                                                   # 1000 1001 1002 1003


#salary=[]
#for emp in employees:                                                     # o/p
#    salary.append(emp.salary)
#print(salary)                                                 #  ['25000', '26000', '28000', '29000']


#salary=[]
#for emp in employees:
#    salary.append(emp.salary)                                         # o/p
#highsal=max(salary)
#print(highsal)                                                    #      29000


#salary = []
#for emp in employees:
#    salary.append(emp.salary)  # o/p
#highsal = max(salary)
#for emp in employees:
#    if(emp.salary==highsal):                                            # o/p
#        print(emp.eid,"=>",emp.salary,"=",emp.ename)              #  1003 => 29000 = "unni"
#print(employee)
#salary = max(list(map(lambda emp: emp.salary, employees)))
#print(salary)



    #def get_salary(emp):
    #    return emp.salary
salaries=list(map(lambda emp:emp.salary,employees))
print(salaries)
highsal=max(salaries)
print(highsal)
                                                       #      o/p
                                                 #['25000', '26000', '28000', '29000']
                                                          # 29000
developer1=list(filter(lambda emp:emp.desig=="developer",employees))
print(developer1)

