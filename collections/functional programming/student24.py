class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
s1=Student(101,"hema","bba",250)                                                  # o/p
print(s1)                                                                      #      hema
s2=Student(102,"hema","bba",200)
s3=Student(103,"hema","bba",150)
studentlist=[]
studentlist.append(s1)
studentlist.append(s2)
studentlist.append(s3)

studenttotal=list(map(lambda stud:stud.total,studentlist))
print(studenttotal)                                                          # [250, 200, 150]
print(max(studenttotal))                                                        # 250