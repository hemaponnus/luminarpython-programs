

# 8/4/21--27

##1

#def add(num1,num2):
#    rwturn num1+num2

##2

#def add(*args):             ## to insert any no of arguments
#    print(args)
#add(10,20,30)
                                          # o/p
                                     # (10,20,30)

##3

#def add(*args):                                ## to insert any no of arguments
#    sum=0                                      ## (* args )-- tuples
#    for num in args:
#        sum+=num
#    return sum
#res=add(10,20,30)
#print(res)
                                            # o/p
                                         ### 60

 ##4

#def print_person_details(*args):
#    print(args)
#print_person_details("ajay","tsr","kakkanadu")
                                                     ## o/p
                                       #('ajay', 'tsr', 'kakkanadu')

## 5

#lst=[10,15,8,20,23,20]
#lst.sort(reverse=True)             # desenting order
#print(lst)                            ## o/p
                             # [23, 20, 20, 15, 10, 8]



## 6

#lst=[10,15,8,20,23,20]
#lst=sorted(lst,reverse=True)            # desenting order
#print(lst)



## 7
                                     # dict format
#def print_person_details(**kwargs):  # kwarges={name="ajay",bthhhhplace="tsr",wplace="kakkanadu"}
#    print(kwargs)
#print_person_details(name="ajay",bthhhhplace="tsr",wplace="kakkanadu")
                                              ## o/p
                        # {'name': 'ajay', 'bthhhhplace': 'tsr', 'wplace': 'kakkanadu'}



## 8

#lst=[10,15,8,20,23,20]
#lst=sorted(lst)            # ascenting order
#print(lst)                    ## o/p
                         ##[8, 10, 15, 20, 20, 23]



## 9

#lst=[10,15,8,20,23,20]
#lst=sorted(lst,reverse=True)                    # descenting order
#print(lst)                                       ## o/p
                                        # [23, 20, 20, 15, 10, 8]



##10  or (4)              ## (tuple-- o/p)

#def print_person_details(*args):
#    print(args)
#print_person_details("ajay","tsr","kakkanadu")

                                                     ## o/p
                                       #('ajay', 'tsr', 'kakkanadu')


## 11 or (7)        ## {dic--o/p}

                                     # dict format
#def print_person_details(**kwargs):              # kwarges={name="ajay",bthhhhplace="tsr",wplace="kakkanadu"}
#    print(kwargs)
#print_person_details(name="ajay",bthhhhplace="tsr",wplace="kakkanadu")

                                              ## o/p
                        # {'name': 'ajay', 'bthhhhplace': 'tsr', 'wplace': 'kakkanadu'}


## 12

#def add(*data):                        #// tuple o/p
#    print(data)
#add("name",100,"amal")                       ## o/p
                                     #('name', 100, 'amal')


# 13

#def add(**data):                           ## // dic
#    print(data)
#add(nm="name",am="amal",va=100)                ## o/p
                                      ##{'nm': 'name', 'am': 'amal', 'va': 100}



## 14

employees={
    1000:{"name":"unni","desig":"pythontrainer","exp":"3"},
    1001:{"name":"amal","desig":"bigtrainer","exp":"2"},
    1002:{"name":"bindhu","desig":"mltrainer","exp":"3"}

}

## 1
##########

#eid=int(input("enter employee id"))
#if(eid in employees):
#    print("eid exist")
#else:
#    print("eid not exist")
                                               ## o/p
                                          ## enter employee id1002
                                               ##  eid exist

##2
########
#eid=int(input("enter employee id"))
#if(eid in employees):
#    print(employees[eid]["name"])
#else:
#    print("eid not exist")

                                                 # 0/p
                                   # enter employee id1002
                                          # bindhu


## 3
########

      # create a fun
      # emp_details(eid=1000)  # empname

# (1) # emp_details(eid=1000) # unni


#def emp_details(**kwargs):             # kwags=1000
#    id=kwargs["eid"]
#    if(id in employees):
#        print(employees[id]["name"])
#    else:
#        print("eid not exist")
#emp_details(eid=1000)
                                        ## o/p
                                      ## unni
                                                    ## emp_details(eid=1000) # unni


# (2) ## emp_details(eid=1000,prop="desig")unni pythontrainer

def emp_details(**kwags):
    id=kwags["eid"]
    prop=kwags["prop"]
    if(id in employees):
        print(employees[id]["name"])
        print(employees[id][prop])
    else:
        print("eid not exist")


emp_details(eid=1000,prop="desig")
                                            # o/p
                                          #unni
                                     #pythontrainer

