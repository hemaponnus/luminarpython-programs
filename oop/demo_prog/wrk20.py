class Student:
    def __init__(self,name,roll,sub,mark):
        self.name=name
        self.roll=roll
        self.sub=sub
        self.mark=mark
    def printval(self):
        print("name:",self.name)
        print("roll:",self.roll)
        print("sub:" ,self.sub)
        print("mark:",self.mark)
    def __str__(self):
        return self.name
f=open("wrk20","r")
for lines in f:
    data=lines.split(",")
    name=data[0]
    roll=data[1]
    sub=data[2]
    mark=int(data[3])
    obj=Student(name,roll,sub,mark)
    if(mark>190):
        obj.printval()

                          ## output
    #    name: anu
    #    roll: 1
    #    sub: bca
    #    mark: 200
    #    name: ajay
    #    roll: 4
    #    sub: bca
    #    mark: 198
    #    name: maya
    #    roll: 5
    #    sub: bba
    #    mark: 195


