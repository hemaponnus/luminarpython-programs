
# 30/3/21--24

              #  java,javascript-this key word

class Employee:
    # eid,ename,desig,salary  ## using constructor
    def __init__(this,eid,ename,desig,salary ):
        this.eid=eid
        this.ename=ename
        this.desig=desig
        this.salary=salary
    def print_emp(self):
        print(self.ename)
e1=Employee(1000,"hema","developer",25000)
e2=Employee(1001,"amal","developer",26000)
e3=Employee(1002,"bindhu","business",28000)
e4=Employee(1003,"unni"," managing director",29000)
employees=[]        # [e1,e2,e3,e4]
employees.append(e1)
employees.append(e2)
employees.append(e3)
employees.append(e4)
#sal=[]
#for emp in employees:
#    sal.append(emp.salary)
#print(sal)                                              # ['25000', '26000', '28000', '29000']

salary=list(map(lambda emp:emp.salary,employees))
print(salary)                                            # [25000, 26000, 28000, 29000]

salary=max(list(map(lambda emp:emp.salary,employees)))
print(salary)                                              # 29000


                                 # output

                         #  [25000, 26000, 28000, 29000]
                         #       29000

