
## 16/3/21--16

            ## read numbers
            ## empty list
            ## append numbers to list
            ## sum


#f=open("numbers","r")
#lst=[]
#for num in f:
#    lst.append(num)
#print(lst)

                               ## output

   #['\n', '\n', ' ## 16/3/21--16\n', '\n', ' 101\n', ' 102\n', ' 103\n', ' 104\n', ' 105\n', ' 106\n', ' 107\n', ' 108\n', ' 109\n', ' 110\n', ' 111\n', ' 112\n', ' 113\n', ' 114\n', ' 115\n', ' 116\n', ' 117\n', ' 118\n', ' 119\n', ' 120']


          # rstrip= used to remove characters
          # lstrip = uesd to remove first character


#f=open("numbers","r")
#lst=[]
#for num in f:
#    lst.append(num.rstrip("\n"))
#print(lst)

                                   ## output
#['', '', ' ## 16/3/21--16', '', ' 101', ' 102', ' 103', ' 104', ' 105', ' 106', ' 107', ' 108', ' 109', ' 110', ' 111', ' 112', ' 113', ' 114', ' 115', ' 116', ' 117', ' 118', ' 119', ' 120']


#f=open("numbers","r")
#lst=[]
#for num in f:
#    lst.append(int(num.rstrip("\n")))
#print(lst)
#print(sum(lst))

                            ## output

#[101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]
#2210