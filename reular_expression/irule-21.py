

 #24/3/21-21

 #1

#import re
#n="helloo"
#x= "\w{6}"
#match=re.fullmatch(x,n)
#if match is not None:
#    print("valid")
#else:
#    print("invalid")

                              # output
                  # helloo              # hello
                  # valid                 # invalid

  #2

#import re
#n="56kg"
#x="\d{2}[a-z]{2}"
#match=re.fullmatch(x,n)
#if match is not None:
#    print("valid")
#else:
#    print("invalid")
                           # output
                            # valid
            #or

#import re
#n="56kg"
#x="\d{2}\w{2}"
#match=re.fullmatch(x,n)
#if match is not None:
#    print("valid")
#else:
#    print("invalid")
                             # output
                             # valid

 #3
