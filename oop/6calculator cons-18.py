
 ## 19/3/21-18

#class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         self.num3=self.num1+self.num2
#         self.num4=self.num1-self.num2
#         self.num5=self.num1*self.num2
#         self.num6=self.num1/self.num2
#     def add(self):
#         print("sum is",self.num3)
#     def diff(self):
#         print("difference is",self.num4)
#     def mul(self):
#         print("multiplication",self.num5)
#     def div(self):
#         print("division is",self.num6)
#obj=Calculator(100,3)
#obj.diff()
#obj.add()
#obj.div()
#obj.mul()
                           ## output

                        #difference is 97
                        #sum is 103
                        #division is 33.333333333333336
                        #multiplication 300


            ### or ######

class Calculator:
     def __init__(self,num1,num2):
         self.num1=num1
         self.num2=num2
     def add(self):
         return self.num1+self.num2
     def diff(self):
         return self.num1-self.num2
     def mul(self):
         return self.num1*self.num2
     def div(self):
         return self.num1/self.num2
obj=Calculator(100,3)
print(obj.diff())
print(obj.add())
print(obj.div())
print(obj.mul())

                            ## output ##
                  #   97
                  #   103
                  #   33.333333333333336
                  #   300
