

   # 30/3/21--24


# lambda functions
#            _____________________________
#   to consise code-to reduce length of code


##1

# def add(num1,num2):
#    return num1+num2                           #  output
# res=add(10,12)                                       #22
# print(res)
# eg

# f=lambda num1,num2:num1+num2                        # output
# res=f(10,12)                                          # 22
# print(res)


# 2

# cube=lambda num:num**3                               # output
# print(cube(6))                                            # 216

# cube=lambda num:num**3                               # output
# res=cube(6)                                            #216
# print(res)


## pre-defined functions

### map()
### filter()
### reduce()

##1
# square of lst

# lst=[10,20,30,21,22]
# for num in lst:                                     #output
#    res=num**2                       #      100,400,900,441,484
#    print(res)

##or

# lst=[10,20,30,21,22]
# squ=[]
# for num in lst:                                     #output
#    res=num**2                       #      [100,400,900,441,484]
#    squ.append(res)
# print(squ)

########## for list allnumbers are integer object#####

###  map()
###  filter()
###  reduce()


              ###### map()

# pass 2 arguments
# 1) function?  which fun to apply each object
# 2)iterables   on which


##1

# lst=[10,20,30,21,22,23,24]                                  # output
# def squ(no):                                    [100, 400, 900, 441, 484, 529, 576]
#    return no**2
# squares=list(map(squ,lst))
# print(squares)

## or

# lst=[10,20,30,21,22,23,24]                                  # output

# squares=list(map(lambda no:no**2,lst))             #   [100, 400, 900, 441, 484, 529, 576]
# print(squares)

# diff linear/binary search

# linear search= 1/1     time waste
# binary search = search by specify eg :vivek, check v

##2
#lst=[45,67,89,90,56,345]
#def cube(no):
#    return no**3
#cubes=list(map(cube,lst))
#print(cubes)

           ## or

#lst=[45,67,89,90,56,345]
#cubes=list(map(lambda no:no**3,lst))
#print(cubes)



                         ## over all


lst=[10,20,30,21,22,23,24]

#def squ(no):                           #         [100, 400, 900, 441, 484, 529, 576]
#    return no**2

squares=list(map(lambda no:no**2,lst))
print(squares)

#def cub(no):
#    return no**3

cubes=list(map(lambda no:no**3,lst))   #  [1000, 8000, 27000, 9261, 10648, 12167, 13824]
print(cubes)

#[100, 400, 900, 441, 484, 529, 576]
#[1000, 8000, 27000, 9261, 10648, 12167, 13824]