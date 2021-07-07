

  # 15/3/21--15

 # Dictionary
###############

               # dic={}
               # print(type(dic))

# key-value pairs

#roll:1001
#name:arun
#age:25

#key: roll,name,age
                                                                               # properties
#1001,arun,25

#student={"roll":1001,"name":"arun","age":25}
#print(student)                                                        # support heterogenious

             #{'roll': 1001, 'name': 'arun', 'age': 25}


#student1={"roll":1001,"name":"arun","age":25,"age":30}
#print(student1)                                                       # duplicate key not allowed

            #{'roll': 1001, 'name': 'arun', 'age': 30}


#student1={"roll":1001,"name":"arun","age":25,"cpp":25}
#print(student1)                                                       # duplicate value support

          #{'roll': 1001, 'name': 'arun', 'age': 25, 'cpp': 25}

                                                                       # insertion order support
#print(student1["age"])
                        # o/p
                          #  25
         ## if we want to fetch a value we have to use corresponding key
#print(student1["name"])
                   # arun

         ##1

#roll: 1001
#name: arun
#age: 25
#cpp': 25

student1={"roll":1001,"name":"arun","age":25,"cpp":25}
#for i in student1:
#    print(i,",",student1[i])
                                       # o/p
                            #     roll, 1001
                            #     name, arun
                            #     age, 25
                            #     cpp, 25

### update
##############

#student1["name"]="arjun"
#student1["age"]=30
#student1["cpp"]+=10
#student1["1001"]=1004

print(student1)

                                         # o/p
                   #{'roll': 1001, 'name': 'arjun', 'age': 30, 'cpp': 35, '1001': 1004}


 ## for delete ##
##################


# del

#del student1["cpp"]                          # o/p
#print(student1)                   {'roll': 1001, 'name': 'arjun', 'age': 30}



### to check ###
##################


#print("total" in student1)                   # o/p
                                          #      False

#print("cpp"in student1)                      # true


### to add ###
#################

#student1["total"]=150                                    # o/p
#print(student1)                #{'roll': 1001, 'name': 'arjun', 'age': 30, 'cpp': 35, 'total': 150}




# collection  # definition  # hetro   # inser  # dupli   # mutable

# list            []            yes      yes      yes        yes
# tuples          ()            yes      yes      yes        no
# set            set()          yes      yes      no         yes
# dic             {}            yes      yes      value      yes