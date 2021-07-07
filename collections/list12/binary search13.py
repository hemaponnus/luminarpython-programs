
  # 8\3\21--13

         # what is binary search?

              # sorting
              # type of soarting
              # seaching selected type
        # what is linear search?
             # checking whole


## algorithm

##1.sorting

#lst=[7,4,1,2,3]
#lst.sort()

# lst=[1,2,3,4,7]                                           lst=[1 2 3 4 7]


      #   low     upp
##2.   low=0                   0
       #upp=length(lst)-1        4


##3. calculate mid

   # mid=(low+upp)//2

   # (0+4)//2=2 ( lst[2])  it will 3 in lst


## 4. condition
   #1. if(element>lst[mid])       4>3
      # low=mid+1
   #2. if(element<lst[mid])       2<3
      # upp=mid-1

  #3. search element==elememt
     # element found



    # example:
  #############

lst=[3,4,2,11,10,13,12,14,15]               # 14
                                        # 2, 3, 4, 10, 11, 12, 13, 14, 15]
lst.sort()
print(lst)
low=0                                           # 0
upp=len(lst)-1                                  #9-1=8
element=int(input("enter element to search"))    #14
flag=0
while(low<=upp):                                # 0<=8        5<=8                 7<=8
    mid=(low+upp)//2                            # (0+8)//2=4   (5+8)//2=6          (7+8)//2=7

    if(element>lst[mid]):                        #14>lst[4]=14>11  14>lst[6]=14>13   14>lst[7]=14>14
        low=mid+1                                # 5               7
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):                                                             #14==14
        flag=1
        break
if(flag>0):
    print("element found")                                                                # ""
else:
    print("element not found")