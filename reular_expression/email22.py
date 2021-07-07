
  # 25/3/21-22

#import re
#x="[a-z0-9]+[@][a-z]+[.]+[a-z]+$"
#mail="hemabkrishnan98@gmail.com"
#match=re.fullmatch(x,mail)
#if match is not None:
#    print("valid")
#else:
#    print("invalid")
                                         ## output
                                            ## valid


        ## or  ##

#import re
#n=input("enter the mail to validate")
#x="([a-zA-z0-9+-]+@[a-zA-z0-9]+\.[a-zA-z0-9]+$)"
#match=re.fullmatch(x,n)
#if match is not None:
#    print("valid")
#else:
#rt    print("invalid")
                                                  # output
                                  # hemabkrishnan98@gmail.com
                                        # valid


                ## or ##

import re
n=input("enter the mail to validate")
x="\w+\d+[@]+\w+\.\w+$"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
                                       # output
                               # hemabkrishnan98@gmail.com
                                       # valid