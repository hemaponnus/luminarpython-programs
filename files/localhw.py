## 16/3/21--16

##1

  ## fname
  ## age
  ## loc

#f=open("local","r")
#for lines in f:
#    data=lines.rstrip("\n").split(" ")
#    fname=data[1]
#    age=data[3]
#    loc=data[-1]
#    print(fname,",",age,",",loc)

                                        ### output####

                                   #hema , 22 , uk
                                   #amal , 22 , uk
                                   #bindhu , 43 , uk
                                   #unni , 50 , uk
                                   #lachu , 23 , uk
                                   #sherin , 26 , uk
                                   #kesia , 25 , uk
                                   #ashu , 25 , uk
                                   #john , 33 , africa
                                   #krithi , 45 , africa
                                   #fruth , 34 , england
                                   #kishore , 56 , india
                                   #anupama , 23 , india

 ##2
### cound number working in each location


#f=open("local","r")
#dic={}
#for lines in f:
#    data=lines.rstrip("\n").split(" ")
#    loc=data[-1]
#    if(loc not in dic):
#      dic[loc]=1
#    else:
#      dic[loc]+=1
#print(dic)

                                 ### output###
                 #{'uk': 8, 'africa': 2, 'england': 1, 'india': 2}


 ##3##
##age  coun

f=open("local","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(" ")
    age=data[-3]
    if(age not in dic):
        dic[age]=1
    else:
        dic[age]+=1
print(dic)

                                    ## output ###
###{'22': 2, '43': 1, '50': 1, '23': 2, '26': 1, '25': 2, '33': 1, '45': 1, '34': 1, '56': 1}



 ##4##
### professional count

#f=open("local","r")
#dic={}
#for num in f:
#    data=num.rstrip("\n").split(" ")
#    pro=data[-2]
#    if(pro in dic):
#        dic[pro]+=1
#    else:
#        dic[pro]=1
#print(dic)


                       ## output ###
## {'it': 4, 'mech': 3, 'beautition': 1, 'elect': 1, 'business': 2, 'nurse': 2}


