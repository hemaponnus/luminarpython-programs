
   ## 19/3/21-18


  ## 3

 ## multiple inheritence     ## inheriting multiple classes

class Parent:
    parent_name = "Arun"

    def m1(self, age):
        self.age = age
        print("my name is", Parent.parent_name)
        print(self.age)


class Mobile:
    def mob(self):
        print("i have 1+")


class Child(Parent, Mobile):
    def m2(self, cage):  # age also
        self.cage = cage  # self.age=age
        print("parent name is", Parent.parent_name)
        print(self.cage)


c = Child()
c.m2(26)
c.m1(22)
c.mob()
                                       ## output

                              #parent name is Arun
                                       #26
                                #my name is Arun
                                       #22
                                  #i have 1+
