
# 23/3/21-20

#import re
#x="[abc]"                               ## either a,b,c
#matcher=re.finditer(x,"abc_c@hjjs")     ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())

     # output
  #  0
  #  a
  #  1
  #  b
  #  2
  #  c
  #  4
  #  c


##############
 ## 2

import re

#x = "[^abc]"                                # except a,b,c
#matcher = re.finditer(x, "abc_c@hjjs")      ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())

      # output #
#    3
#    _
#    5
#    @
#    6
#    h
#    7
#    j
#    8
#    j
#    9
#    s

############
 ##3

#x = "[a-z]"                                # check a-z
#matcher = re.finditer(x, "abc_c@hjjs")      ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())

              ## output
 #   0
 #   a
 #   1
 #   b
 #   2
 #   c
 #   4
 #   c
 #   6
 #   h
 #   7
 #   j
 #   8
 #   j
 #   9
 #   s


############
### 4


#x = "[A-Z]"                                # check A-Z
#matcher = re.finditer(x, "Aabc_c@hjjs")      ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())

        # output
    # 0
    # A

#######
###5

#x = "[a-zA-Z]"                                # check both a-z A-Z
#matcher = re.finditer(x, "Aabc_c@hjjs")      ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())
                      ## output
 #   0
 #   A
 #   1
 #   a
 #   2
 #   b
 #   3
 #   c
 #   5
 #   c
 #   7
 #   h
 #   8
 #   j
 #   9
 #   j
 #   10
 #   s

###########
##6


#x = "[0-9]"                                # check both 0-9
#matcher = re.finditer(x, "Aabc_c@hjj1s")      ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())

    #output
  #10
   # 1

##7

#x = "[^a-zA-z0-9]"                                # check symbols
#matcher = re.finditer(x, "Aabc c@hjj1s")      ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())

       ## output
       #6
       #@

####
##8

#x = "\s"                                      ## check space
#matcher = re.finditer(x, "Aabc c@hjj1s")      ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())

          #output
          #4
          #

 ## 9

#x = "\d"                                     # check digits
#matcher = re.finditer(x, "Aabc c@hjj1s")      ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())

        ##output
          # 10
          # 1

###10

#x = "\D"                                  ## except digits
#matcher = re.finditer(x, "Aabc c@hjj1s")  ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())

    ##output
    # 0
    # A
    # 1
    # a
    # 2
    # b
    # 3
    # c
    # 4
    #
    # 5
    # c
    # 6
    # @
    # 7
    # h
    # 8
    # j
    # 9
    # j
    # 11
    # s


##########
## 11

#x = "\w"                                  ##  check words except special charecters
#matcher = re.finditer(x, "Aabc c@hjj1s")  ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())

    ##output
 #   0
 #   A
 #   1
 #   a
 #   2
 #   b
 #   3
 #   c
 #   5
 #   c
 #   7
 #   h
 #   8
 #   j
 #   9
 #   j
 #   10
 #   1
 #   11
 #   s

#####
##12

#x = "\W"                                   ##  check special charecters except words
#matcher = re.finditer(x, "Aabc c@hjj1s")   ## check abc
#for match in matcher:
#    print(match.start())
#    print(match.group())

       ## output
      # 4
      #
      # 6
      #@

 ####
 #13
      ##or
#x ="[^a-zA-Z0-9]"                           ##  check special charecters except words
#matcher = re.finditer(x, "Aabc c@hjj1s")     ## check abc
#for match in matcher:
#    print(match.start())
#   print(match.group())

                      #output
      # 4
      #
      # 6
      # @