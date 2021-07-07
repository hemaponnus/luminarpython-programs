
  # 12\3\21--14

    # read value from console and print its paired values

#lst=[1,2,3,4,5,6]
#num=int(input("enter a num"))
#flag=0
#for i in lst:
#    if(num==i):
#      flag=1
#      break
#    else:
#       pass
#if(flag==0):
#   print("num not found")
#else:
#   print("found")
#   for i in lst:
#       for j in lst:
#           print(i,",",j,"=",i+j)
#           if(i+j==num):
#               print("paired values are","(", i," ,",j,")")


           ### or####


lst=[1,2,3,4,5,6]
num=int(input("enter a num"))
flag=0
for i in lst:
    if(num==i):
      flag=1
      break
    else:
       pass
if(flag==0):
   print("num not found")
else:
   print("found")
   for i in lst:
       for j in lst:
           if(i+j==num):
               print("paired values are : ""(", i," ,",j,")")