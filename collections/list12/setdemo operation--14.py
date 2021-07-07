
   ## 12/3/21--14

                ##### operations #####

# union                         # set3=set1.union(set2)
# intersection                  # set3=set1.intersection(set2)
# difference

set1={1,2,3,4,5,6}
set2={5,6,7,8,9,10}

## union=1,2,3,4,5,6,7,8,9,10

#set3=set1.union(set2)
#print(set3)                                       #       {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

## intersection=5,6

#set4=set1.intersection(set2)
#print(set4)                                        #       {5, 6}

## difference
# set1-set2

#set5=set1.difference(set2)
#print(set5)                                               # {1, 2, 3, 4}

set6=set2.difference(set1)
print(set6)                      # {8, 9, 10, 7}0

 #