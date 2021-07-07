
# 31/3/21-25


from functools import reduce

lst=[10,20,30,50,80]
total=reduce(lambda no1,no2:no1+no2,lst)
print(total)                                                           # o/p
                                                                        #190
#if(no<0):
#    return -ve
#else:
#      return +ve
#-ve if no<0 else + ve

                          # or

mx=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(mx)                                                                  # o/p
                                                                           #  80

min=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(min)                                                                 # o/p
                                                                           #  10