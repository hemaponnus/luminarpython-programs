
 #24/3/21-21


  ##1

#import re
#x="a+"                                # a including group
#r="wwwawwefkol aaabc dasg 13a@"
#matcher=re.finditer(x,r)
#for match in matcher:
#    print(match.start())
#    print(match.group())

                     # output
    #3
    # a
    #12
    #aaa
    #19
    #a
    #25
    #a

 ##2

#import re
#x="a*"                                # count including zero num of a(group)
#r="aawwa aaabcdasg 13a@"
#matcher=re.finditer(x,r)
#for match in matcher:
#    print(match.start())
#    print(match.group())

    # output
   # 0
   # aa
   # 2

   # 3

   # 4
   # a
   # 5

   # 6
   # aaa
   # 9

   # 10

   # 11

   # 12
   # a

   # 13

   # 14
   # a
   # 15

   # 16

   # 17

   # 18
   # a
   # 19

   # 20


##3

#import re
#x="a?"                        # count a as each including zero num of a individual
#r="aawwa aaabcdasg 13a@"
#matcher=re.finditer(x,r)
#for match in matcher:
#    print(match.start())
#    print(match.group())

              # output
    # 0
    # a
    # 1
    # a
    # 2

    # 3

    # 4
    # a
    # 5

    # 6
    # a
    # 7
    # a
    # 8
    # a
    # 9

    # 10

    # 11

    # 12
    # a

    # 13

    # 14
    # a
    # 15

    # 16

    # 17

    # 18
    # a
    # 19

    # 20

#4

#import re
#x="a{3}"                        # no of a position of 3a
#r="asddaaa adreaa "
#matcher =re.finditer(x,r)
#for match in matcher:
#    print(match.start())
#    print(match.group())
                            ## output
                            #4
                            #aaa
##5

import re

#x="a{1,3}"                               ##min 1 max 3
#r="aadaaaa adreaa"
#matcher=re.finditer(x,r)
#for match in matcher:
#    print(match.start())
#    print(match.group())
                           ## output
 #   0
 #   aa
 #   3
 #   aaa
 #   6
 #   a
 #   8
 #   a
 #   12
 #   aa



 ##6

#x="^a"                          ## check starting with a
#r="asddaaa adreaa "
#matcher =re.finditer(x,r)
#for match in matcher:
#    print(match.start())
#    print(match.group())
                ##output
                 #0
                 #a

##7

#x="a$"                          ## check ending with a
#r="asddaaa adreaa"
#matcher =re.finditer(x,r)
#for match in matcher:
#    print(match.start())
#    print(match.group())

           ## output
             # 13
             # a


  ## next: irule-21.py