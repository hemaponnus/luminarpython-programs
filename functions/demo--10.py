

   #3/3/21--10

                          ## Functions####

        ## functions are used to perform some tasks


   ##1

#num1=int(input("enter first num"))
#num2=int(input("enter second num"))
#sum=num1+num
#print(sum)                                        # gets our output


   ##2
#num1=int(input("enter first num"))
#num2=int(input("enter second num"))
#sum=num1+num
#print(sum) #num1=int(input("enter first num"))
#num2=int(input("enter second num"))
#sum=num1+num
#print(sum)
                               ## we need to repeat the code each time to get output again



          ### To overcome this we use functions in python

##### functions ######

      ##to perform some task,we set some instructions as code as function
       ## instruction-->code-->function

## some inbuild functions in Python

          ## print  (print in console)
          ## input  ( read/ call message from console )
          ## type   (pre-defined functions)

          ## sum (only in collection,list)not function



                        ##### Syntax  #####
                 ########################################


#def functionname(arguments):
#    function definition

#function call   ##using function name


           ## 3- Methods

  # 1.  function without an arguments and no return type
  # 2.  function with arguments and no return type
  # 3.  function with arguments and return type



      #### 1.  function without an arguments and no return type  ###


  ##1
       ##additon

                                                           ## O/p
#def add():
#    num1=int(input("enter 1 st number"))                enter 1 st number23
#    num2=int(input("enter 2 nd number"))                enter 2 nd number24
#    sum=num1+num2                                               47
#    print(sum)
#add()
#add()


  ##2
          ##substraction


#def sub():
#    num1=int(input("enter 1 stnum"))
#    num2=int(input("enter 2nd num"))
#    dif=num1-num2
#    print(dif)
#sub()
#sub()


 ##3

   ##multiplication

#def multi():
#    num1=int(input("enter 1st num"))
#    num2=int(input("enter 2nd number"))
#    multi=num1*num2
#    print(multi)
#multi()
#multi()


        ###  2. function with arguments and no return type

##1

#def addition(num1,num2):                               0/p
#    sum=num1+num2
#    print(sum)                                        28
#addition(13,15)

##2
                                                        # 0/p

#def substra(num1,num2,num3):                            5
#    min=num1-num2-num3
#    print(min)
#substra(13,3,5)


        ####  3.function with arguments and return type


 ##1
                                                                ### o/p

#def sumn(num1,num2):                                          40
#    sum=num1+num2
#    return sum
#data=sumn(15,25)     ## variable declaration
#print(data)


 ##2
                                              ## o/p
#def sub(num1,num2):
#   min=num1-num2                                    9
#   return min
#bingo=sub(26,17)
#print(bingo)


 ##3
                                                ## o/p
#def multi(num1,num2,num3):
#    mul=num1*num2*num3                            24
#    return(mul)
#pipa=multi(2,3,4)
#print(pipa)
