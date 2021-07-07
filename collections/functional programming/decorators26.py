# 7/4/21--26

                      ## Decorators ##


                    # changing without changing function


#def sub(num1,num2):
#    if num1<num2:
#        (num1,num2)=(num2,num1)
#    return num1-num2
#res=sub(80,20)
#print(res)

          ## or


#ef sub(num1,num2):
#    if num1<num2:
#        temp=num1
#        num1=num2
#        num2=temp
#    return num1-num2
#res=sub(20,80)
#print(res)
                                                     #o/p
                                                        #60


  ## 1
#############################


#def decorator_sub(fun): # sub(20,80
#    def inner(num1,num2):  # (20,80)   # //inner//wrapper
#        if num1<num2:      # 20<80
#            (num1,num2)=(num2,num1)  # (80,20)
#        return fun(num1,num2)        #  sub(80,20)
#    return inner

#@decorator_sub        #sub=(80,20)
#def sub(num1,num2):
#    return num1-num2
#res=sub(20,80)
#print(res)


##2

def div_dedcorator(fun):
    def wrapper(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
        return fun(num1,num2)
    return wrapper
@div_dedcorator
def div(num1,num2):
    return num1/num2
res=div(2,10)
print(res)                                             #o/p
                                                  ### 0.5



#############################################################################################################


##  git and github 1.5 hr
##  database 4 hr
##  mysql

## mysql download--community dwnload--mysql installer for windows--422.4M --dwmload