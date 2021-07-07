#1


# read bitrh month
#       "     day
#       "     year

#  current  date
#        "  month
#         " year

# current age
                                                               #output

birthmonth=int(input("enter the birth month"))
birthday=int(input("enter the birth day"))
birthyear=int(input("enter the birth year"))
currentday=int(input("enter current date"))
currentmonth=int(input("enter current month"))
currentyear=int(input("enter current year"))
age=currentyear-birthyear
if currentmonth>=birthmonth:
    if(currentday>=birthday):
        print("age",age)
    else:
         print("age is",age-1)
elif(currentmonth<=birthmonth):
   print("age is",age-1)
