
   #25|2|21--7


      #      read 4 sub and calculate threir percentage

            # 4 sub mark
            # cal per
            # tot mark 200
            # abo 90-     A+
               #  80-89   A
               #  70-79   B+
               #  60-69   B
               #  50-59   C+
               #  40-49   C
               #  30-39   D+
               #fail


num1=int(input ("enter the mark of english sub"))
num2=int(input("enter the mark of mala sub"))
num3=int(input("enter the mark of hindi sub"))
num4=int(input("enter the mark of bio sub"))
total=num1+num2+num3+num4
perc=(total/200)*100
if(perc>=90):
    print("grade is A+")
elif(80<=perc<=89):
    print("grade is A")
elif(70<=perc<=79):
    print("grade is B+")
elif(60<=perc<=69):
    print("grade is B")
elif(50<=perc<=59):
    print("grade is C+")
elif(40<=perc<=49):
    print("grade is C")
elif(30<=perc<=39):
    print("grade is D+")
else:
    print(" fail")
