
 # 7/4/21--26



               ## add operator
        #################################

#class Book:
#    def __init__(self,pages):
#        self.pages=pages
#    def __add__(self, other):                               #  work when add operators find
#        return "hello"
                     # num=int(10)        ## 10 int type
                     # b5=str("hello")    ## hello str type

#b1=Book(100)                                  ## Book type
#b2=Book(200)                                   ## Book type
#print(b1+b2)                                                          # error


##2

#class Book:
#    def __init__(self,pages):
#        self.pages=pages
#    def __add__(self, other):
#        return self.pages+other.pages

#b1=Book(100)
#b2=Book(200)
#print(b1+b2)
                                                         #0/p
                                                        # 300

##3

#class Book:
#    def __init__(self, pages):
#        self.pages = pages

#    def __add__(self, other):
#        return Book(self.pages+other.pages)
#    def __str__(self):
#        return str(self.pages)


#b1=Book(100)
#b2=Book(200)
#b3=Book(300)
#b4=Book(400)
#print(b1+b2+b3+b4)                                            ## o/p
                                                              ##1000


##4
                                 ## sub operator
                        ###################################
#class Book:
#    def __init__(self, pages):
#        self.pages = pages

#    def __sub__(self, other):
#        return Book(self.pages-other.pages)
#    def __str__(self):
#        return str(self.pages)


#b1=Book(100)
#b2=Book(200)
#b3=Book(300)
#b4=Book(400)
#print(b1-b2)



##5

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __mul__(self, other):
        return Book(self.pages*other.pages)
    def __str__(self):
        return str(self.pages)


b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(400)
print(b1*b2)                                                   ## o/p
                                                            # 20000

##6
#class Book:
#    def __init__(self, pages):
#        self.pages = pages

#    def __truediv__(self, other):
#        return Book(self.pages/other.pages)
#    def __str__(self):
#        return str(self.pages)


#b1=Book(100)
#b2=Book(200)
#b3=Book(300)
#b4=Book(400)
#print(b1/b2)                                                       ## o/p
                                                                ##  0.5


            ##############################################################3

 ########## overall###########

#class Book:
#    def __init__(self, pages):
#        self.pages = pages
#   def __add__(self, other):
#        return Book(self.pages+other.pages)
#    def __sub__(self, other):
#        return Book(self.pages-other.pages)
#    def __mul__(self, other):
#     return Book(self.pages * other.pages
#    def __truediv__(self, other):
#        return Book(self.pages/other.pages)

#    def __str__(self):
#        return str(self.pages)


#b1=Book(100)
#b2=Book(200)
#b3=Book(300)
#b4=Book(400)
#print(b1-b2)