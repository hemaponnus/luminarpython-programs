
   #18/3/21-17

               ## finally block

            # work same time at try block ,except block

lst=[1,2,3,4]
a=int(input("index"))
try:                                     #4                  0
    print(lst[a])
except Exception as e:
    print("exception")                  # exception          1
finally:
    print("inside finally")             # inside finally    inside finally