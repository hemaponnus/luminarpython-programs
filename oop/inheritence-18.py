
  ## 19/3/21-18


              ## inheritence - to choose  attribute and method of one class to another class


  #(1)    ## single inheritence
  #(2)    ## multiple inhertence
  #(3)    ## multi-level



     #(1) single inheritance
  ###################################


  ##1

#class Parent:                                               ## parent/base/super class
#    parent_name="Arun"
#    def m1(self,age):
#        self.age=age
#        print("my name is",Parent.parent_name)
#        print(self.age)
#class Child(Parent):                                       ## derived/child/
#   def m2(self):
#        print("parent name is",Parent.parent_name)
#        print(self.age)
#c=Child()
#c.m1(22)
#c.m2()

                                  ## output

                            #my name is Arun
                               #22
                           #parent name is Arun
                                   #22

                 ## or

#class Parent:
#    parent_name="Arun"
#    def m1(self,age):
#        self.age=age
#        print("my name is",Parent.parent_name)
#        print(self.age)
#class Child(Parent):
#    def m2(self,cage):                                  # age also
#        self.cage=cage                                  # self.age=age
#        print("parent name is",Parent.parent_name)
#        print(self.cage)
#c=Child()
#c.m1(22)
#c.m2(26)
                                     ### output
                                 #my name is Arun
                                  #22
                                #parent name is Arun
                                     #26



          ### eg:

  ##2

#class Student:
#    clg_name="Rohini college"
#    def st1(self,id,name,age):
#        self.id=id
#        self.name=name
#        self.age=age
#        print("id",self.id)
#        print("name",self.name)
#        print("age",self.age)
#        print("clg_name",Student.clg_name)
#class Teac(Student):
#        def teac(self,sub):
#            self.sub=sub
#            print("sub",self.sub)
#            print("clg_name",Student.clg_name)
#            print("age",self.age)
#obj=Teac()
#obj.st1(123," weeerr",21,)
#obj.teac("eng")


                                   ## output


                                     #id 123
                                  #name  weeerr
                                   #age 21
                            #clg_name Rohini college
                                   # sub eng
                            #clg_name Rohini college
                                  # age 21

    ## 3

      ## multiple inheritence     ## inheriting multiple classes

class Parent:
    parent_name="Arun"
    def m1(self,age):
        self.age=age
        print("my name is",Parent.parent_name)
        print(self.age)
class Mobile:
    def mob(self):
        print("i have 1+")
class Child(Parent,Mobile):
    def m2(self,cage):                                  # age also
        self.cage=cage                                  # self.age=age
        print("parent name is",Parent.parent_name)
        print(self.cage)
c=Child()
c.m1(22)
c.m2(26)
c.mob()