lst=[4,2,1,6,7,8]

 # output :3,1,0,7,8,9
updatelist=[]
for i in lst:
    if(i<5):
        i-=1
        updatelist.append(i)
    else:
        i+=1
        updatelist.append(i)                                                # o/p
print(updatelist)                                                    # [3, 1, 0, 7, 8, 9]



result=list(map(lambda num:num-1 if num<5 else num+1,lst))                  # o/p
print(result)                                                        # [3, 1, 0, 7, 8, 9]


#if num<5;
#     num-1
#else:
#     num+1