
  # 29/3/21--23

           # add two numbers()

    # camalin notation -- addTwonumbers()
    #python snake notation-- add_twonumbers(
#class Person:
#    def set_person(self):


#obj=Person()
#lst=List()
#list.append(100)
#from builtins import *
#lst=list()

##1

#def add(num1,num2):
#    return num1+num2                           #  output
#res=add(10,12)                                       #22
#print(res)

##1.1

#add=lambda num1,num2:num1+num2                         # output
#print(add(100,200))                                       # 300


##2
#sub=lambda num1,num2:num1-num2                         # output
#print(sub(300,200))                                       #100

#__________________________________________________________________________________________________________



   # 29/3/21--23


                #lambda functions
#            _____________________________
#   to consise code-to reduce length of code


##1

#def add(num1,num2):
#    return num1+num2                           #  output
#res=add(10,12)                                       #22
#print(res)
             #eg

#f=lambda num1,num2:num1+num2                        # output
#res=f(10,12)                                          # 22
#print(res)


#2

#cube=lambda num:num**3                               # output
#print(cube(6))                                            # 216

#cube=lambda num:num**3                               # output
#res=cube(6)                                            #216
#print(res)


## pre-defined functions

    ### map()
    ### filter()
    ### reduce()

##1
   # square of lst

#lst=[10,20,30,21,22]
#for num in lst:                                     #output
#    res=num**2                       #      100,400,900,441,484
#    print(res)

 ##or

#lst=[10,20,30,21,22]
#squ=[]
#for num in lst:                                     #output
#    res=num**2                       #      [100,400,900,441,484]
#    squ.append(res)
#print(squ)

########## for list allnumbers are integer object#####



                     ###  map()
                     ###  filter()
                     ###  reduce()



                   #pass 2 arguments
                   #1) function?  which fun to apply each object
                   #2)iterables   on which

#lst=[10,20,30,21,22,23,24]                                  # output
#def squ(no):                                    [100, 400, 900, 441, 484, 529, 576]
#    return no**2
#squares=list(map(squ,lst))
#print(squares)

## or

#lst=[10,20,30,21,22,23,24]                                  # output

#squares=list(map(lambda no:no**2,lst))             #   [100, 400, 900, 441, 484, 529, 576]
#print(squares)

     # diff linear/binary search

# linear search= 1/1     time waste
#binary search = search by specify eg :vivek, check v


   ## 25/3/21-31

# lst=[10,20,30,21,22,23,24]


# def squ(no):
#    return no**2

# squares=list(map(lambda no:no**2,lst))
#

# print(squares)
#
#
#
# cubes=list(map(lambda no:no**3,lst))
# print(cubes)


#filter(function,iterables)
#even=list(filter(lambda num:num%2==0,lst))                              # o/p
#print(even)                                                   #     [10, 20, 30, 22, 24]


#lst=["akhil","aravind","akash","varun,vibin","ram"]
#aname=list(filter(lambda name:name[0]=='a',lst))                          # o/p
#print(aname)                                                  #      ['akhil', 'aravind', 'akash']
