#24/3/21-21
#import re
#n=input("enter the num to validate")
#x="\d{10}"
#match=re.fullmatch(x,n)
#if match is not None:
#    print("valid")
#else:
#    print("invalid")


                              ## output
            # enter the num to validate1: 234567890
                         # valid
            # enter the num to validate1: 1234
                         # invalid

#2

#import re
#n=input("enter a number")
#x="^91\d{10}"
#match=re.fullmatch(x,n)
#if match is not None:
#    print("valid indian no")
#else:
#    print("invalid indian no")

                             # valid
          # enter   a number + 911234567890
           #           valid  indian no
         # enter   a number + 911890
           #          invalid  indian no

                ####or ##

import re
n=input("enter a number")
x="[+][9][1]\d{10}"
match=re.fullmatch(x,n)
if match is not None:
    print("valid indian no")
else:
    print("invalid indian no")
                             ## output
               # enter   a number + 911234567890
                  #           valid  indian no
               # enter a number +91567
                   #         invalid  indian no