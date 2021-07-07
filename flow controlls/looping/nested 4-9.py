
    # 1/3 /21--9


                 # 10 9 8 7 6 5 4 3 2 1
                 # 9 8 7 6 5 4 3 2 1
                 # 8 7 6 5 4 3 2 1
                 # 7 6 5 4 3 2 1
                 # 6 5 4 3 2 1
                 # 5 4 3 2 1
                 # 4 3 2 1
                 # 3 2 1
                 # 2 1
                 # 1

#for i in range(11,0,-1):
#    for j in range(i-1,0,-1):
#        print(j,end=" ")
#    print()

                                  ## or
#for i in range(1,11):
#    for j in range(11-i,0,-1):
#        print(j,end=" ")
#    print()



     ##2


                           # 1
                           # 2  2
                           # 3  3  3
                           # 4  4  4  4
                           # 5  5  5  5  5




#for i in range(1,6):              #  1  2 3  4 5
#    for j in range(1,i+1):        #1(1) 2(1) 2(2) 3(1) 3(2)  3(3)
#        print(i,end=" ")
#    print()



     ##3


                             # 1 1 1 1 1
                             # 2 2 2 2
                             # 3 3 3
                             # 4 4
                             # 5


#for i in range(1,6):
#    for j in range(5,i-1,-1):
#        print(i,end=" ")
#    print()



      ##4


                             # 4 4 4 4
                             # 3 3 3
                             # 2 2
                             # 1



#for i in range(4,0,-1):          # i=4                #3       #2    #1
#    for j in range(4,4-i,-1):    #(4,((4-1))-i,-1)
#        print(i,end=" ")         # 4,(3)-i,-1)
#    print()                      # 4,(3-4),-1)
                                 # 4, 1,-1
                                 #  4, 3,2,1           4 3 2   4 3    4
                                 #4(4)4(3)4(2)4(1)  3(4)3(3)3(2)    2(4)2(3)  1(4)





     ##5


                             # 5 5 5 5 5
                             # 4 4 4 4
                             # 3 3 3
                             # 2 2
                             # 1



#for i in range(5,0,-1):
#    for j in range(5,5-i,-1):
#        print(i,end=" ")
#     print()




         ##6


                           # 0 1 2 3 4 5
                           # 0 1 2 3 4
                           # 0 1 2 3
                           # 0 1 2
                           # 0 1



#for i in range(0,6):
#    for j in range(0,7-i):
#        print(j,end=" ")
#    print()



      ## 7


                            # 0 1 2 3 4 5
                            # 0 1 2 3 4
                            # 0 1 2 3
                            # 0 1 2
                            # 0 1
                            # 0

#for i in range(0,6):
#    for j in range(0,6-i):
#        print(j,end=" ")
#    print()
