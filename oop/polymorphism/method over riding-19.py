# 22/3/21-19


            ## child class will override parent class,if both have same method
class Parent:
    def properties(self):
        print("10 lack rs,2 car")
    def marry(self):
        print("with ram")
class Child(Parent):
    def marry(self):
        print("with arun")
c=Child()
c.marry()
                        # output
                            #with arun