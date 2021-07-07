
  #18/3/21-17

               ## Exception handling

        ## is used to clear unexcepted errors

             ## try block
             ## except block

  ##1

#a=int(input("enter a no1"))           # 6
#b=int(input("enter a no2"))           # 0
#c=a/b
#print(c)                               # error

 ##2

#no1=int(input("enter a no1"))       #6                 6
#no2=int(input("enter a no1"))       # 2                0
#try:
#    res=no1/no2
#    print("res",res)                # res 3.0
#except:
#    print("exception occured")                    #exception occured


  ##3

#a=[1,2,3]
#print(a[7])           #error

  ##3.1

#a=[1,2,3,4,5,6,7,8,9,10]
#try:
#    print(a[11])                       #11                7
#except:
#    print("exception occured")         # exce occ          8




  ##3.2


#lst=[1,2,3,4]
#try:
#    i=int(input("index"))               #4                 0
#    print(lst[i])
#except Exception as e:
#    print("exception")                  # exception         1



