
  # 12/3/21--14


##1

               ##     remove duplicates from lst


                                                                          # o/p
#lst=[10,10,20,20,25,25,85,41,41,25,58]
#lst1=set(lst)
#print(lst1)                                                     #  {41, 10, 20, 85, 25, 58}



##2


  ## nested list
##################
                                                                ## o/p
employee=[[1001,"arun",15000],
          [1002,"arjun",20000],
          [1003,"vinu",25000],
          [1004,"binu",1000]]
print(employee)

                        #[[1001, 'arun', 15000], [1002, 'arjun', 20000], [1003, 'vinu', 25000], [1004]]


#for i in employee:
#    print(i)                                  #       [1001, 'arun', 15000]
                                               #        [1003, 'vinu', 25000]
                                               #        [1003, 'vinu', 25000]
                                               #        [1004, 'binu', 1000]

 ## arun
 ## arjun
 ## vinu
 ## binu

#for i in employee:                                      # o/p
#    print(i[1])
                                                    #      arun
                                                    #      arjun
                                                    #      vinu
                                                    #      binu

 ##3

     ## print salary name who salary greater than 17000


                                                        ## o/p
employee=[[1001,"arun",15000],
          [1002,"arjun",20000],
          [1003,"vinu",25000],
          [1004,"binu",1000]]
#for i in employee:
#   if(i[2]>=17000):                                     # arjun
#       print(i[1])                                      # vinu


       ## sum of employee salary
                                                             # o/p
sum=0
for i in employee:
    sum=sum+i[2]
print(sum)                                                  #  61000




