  ## list comprehension


## 1

#lst=[1,2,3,4]
#lst2=[10,20]


            # (1,10)(1,20)(2,10),(2,20),(3,10),(3,20),(4,10),(4,20)

#output=[]
#for i in lst:
#    for j in range:
#        output.append((i,j))
#print(output)
                                          ### o/p

              #[(1, 10), (1, 20), (2, 10), (2, 20), (3, 10), (3, 20), (4, 10), (4, 20)]


 ##2
                 ## sqares of list

#lst=[1,2,3,4]
#squares=[num**2 for num in lst]
#print(squares)

                                               ## o/p
                                            #[1, 4, 9, 16]

## 3
                  # even of list

#lst1=[1,2,3,4,5,6]
#even=[num for num in lst1 if num%2==0]
#print(even)
                                                        ## o/p
                                                    #[2, 4, 6]

## 4 or (1)


lst=[1,2]
lst2=[10,20]
pairs=[(i,j) for i in lst for j in lst2]
print(pairs)
                                                        ## o/p
                                        # [(1, 10), (1, 20), (2, 10), (2, 20)]