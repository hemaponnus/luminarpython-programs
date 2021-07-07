
 #5\3\21--12


  ## list

       # 1. how to define


#lst=[]                        # square bracket   #empty list
#st=list()
#print(type(lst))
#print(type(st))

       # 2. check heterogeneous data support


#lst1=[10,10.5,"luminar","python",True]
#print(lst)

       #3. check Duplicate value allowed

#lst2=[10,10,10.5,"hema","hema"]
#print(lst2)

      # 4. insertion order preserved or not

#lst3=[True,10,10,False,10.5,"hema","hema"]
#print(lst3)

      # 5. Mutable  or imutable

#lst=[10,8,7,9,1,2,100,45,"hema"]
      #     0 to     n-1   # index value 0 to n-1
      # index value
#print(lst[2])                                      # 7
#print(lst[5])                                      # 2
#lst[1]=50
#print(lst)                                        #[10, 50, 7, 9, 1, 2, 100, 45]
#lst[8]="luminar"
#print(lst)                                      #[10, 50, 7, 9, 1, 2, 100, 45, 'luminar']