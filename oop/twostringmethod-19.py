

   #22/3/21-19

class College:
    collegename="lt"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def printval(self):
        print("college name",College.collegename)
        print("name of student",self.name)
        print("roll no",self.roll)
    def __str__(self):
        return self.name+str(self.roll)
obj=College("anu",13)
print(obj)
obj.printval()