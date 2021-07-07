

          # 25/3/21-22

      #1    # combination of uppercase and lowercase letters ending with number

#import re
#x="[a-zA-Z]+\d$"          # x="[a-zA-Z]+\d"
#num=input("enter something")
#match=re.fullmatch(x,num)
#if match!=None:
#   print("valid")
#else:
#   print("invalid")
                                             # output
                                  # enter something    QWas2
                                        #valid

       #2      # starting with a ending with b

#import re
#x="(^a+[a-zA-Z0-9]+b$)"
#num=input("enter something")
#match=re.fullmatch(x,num)
#if match!=None:
#   print("valid")
#else:
#   print("invalid")
                                                # output
                                   # enter something   aAWsefdfkb
                                      # valid

    # 3             # min 8 max 15
            # except num


#import re
#x="\w\D{8,15}"
#num=input("enter something")
#match=re.fullmatch(x,num)
#if match!=None:
#   print("valid")
#else:
#   print("invalid")
                                               # output
                                      # enter something       asdfghjklqwerty
                                               # valid