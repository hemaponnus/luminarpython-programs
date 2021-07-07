

  # 23/3/21-20


 # regular expression - is used to pattern matching

 #using module- recular expression module-re module

 # re -- package for pattern matching/regular expression

 # main use:
 #       for validation


#import re
#count=0
#matcher=re.finditer('ad','adbdfeadtuadadetdfad')
#for match in matcher:
#    count+=1
#print("count=",count)

                          # output #

                         # count= 5


                ## or ##

#import re
#count=0
#matcher=re.finditer('ad','adbdfeadtuadadetdfad')
#for match in matcher:
#    print("match available at=",match.start())
#    print("group=",match.group())
#    count+=1
#print("count=",count)
1
                 ## output ##

               #match available at= 0
               #group= ad
               #match available at= 6
               #group= ad
               #match available at= 10
               #group= ad
               #match available at= 12
               #group= ad
               #match available at= 18
               #group= ad
               #count= 5





