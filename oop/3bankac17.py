# 18/3/21-17


#class Bank:
#    def accreate(self,acno,name,bankname):
#        self.bankname=bankname
#        self.name=name
#        self.acno=acno
#        self.minibal=5000
#        self.bal=self.minibal
#    def deposit(self,amt):
#        self.bal+=amt
#        print("your account has credited with amt",amt)
#        print("your current balance",self.bal)
#    def withdrawn(self,amt):
#        if amt>self.bal:
#            print("insufficient balance")
#        else:
#            print("account debited with",amt)
#            self.bal-=amt
#            print("available balance",self.bal)
#obj=Bank()
#obj.accreate(1233,"jithu","icici")
#obj.deposit(250000)
#obj.withdrawn(1500)

                                ## output

#your account has credited with amt 250000
#your current balance 255000
#account debited with 1500
#available balance 253500

    ## types of variables:

# instance variable- (variables using self)  -    (related to object)
# static variable- (can access using class name)- (related  to class)


class Bank:
    bankname="sbi"                                 ## static variable
    def accreate(self,acno,name,):
        self.name=name
        self.acno=acno
        self.minibal=5000
        self.bal=self.minibal
    def deposit(self,amt):
        self.bal+=amt
        print("your", Bank.bankname,"account has credited with amt",amt)    ## using class name
        print("your current balance",self.bal)
    def withdrawn(self,amt):
        if amt>self.bal:
            print("insufficient balance")
        else:
            print("account debited with",amt)
            self.bal-=amt
            print("available balance",self.bal)
obj=Bank()
obj.accreate(1233,"jithu")
obj.deposit(250000)
obj.withdrawn(1500)

                               ## output
#your sbi account has credited with amt 250000
#your current balance 255000
#account debited with 1500
#available balance 253500