class Addition:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.num3=self.num1+self.num2
    def printval(self):
        print("num3",self.num3)
obj=Addition()
obj.sum(7,5)
obj.printval()

                                  ## output

                                    #num3 12