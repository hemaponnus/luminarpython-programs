
   # 25/3/21-22

import re
lst=[]
x="\w{2}\d{2}\w{2}\d{4}"
f=open("vehnum22","r")
for lines in f:
    data=lines.rstrip("\n")
    match=re.fullmatch(x,data)
    if match is not None:
        lst.append(lines)
print(lst)
                                    ## output
               #['kl09au2345\n', 'kl23er1234\n', 'kl98TM5687\n']


      ## or ##



#import re
#lst = []
#x = "[kK][lL]\d{2}[a-zA-z]{2}\d{4}$"
#f = open("vehnum22", "r")
#for lines in f:
#    match = re.fullmatch(x,lines.rstrip("\n"))
#    if match is not None:
#        lst.append(lines)
#print(lst)

                                        ## output
                  # ['kl09au2345\n', 'kl23er1234\n', 'kl98TM5687\n']


    ## or ##


import re
#lst = []
#lst1=[]
#x = "[kK][lL]\d{2}[a-zA-z]{2}\d{4}$"
#f = open("vehnum22", "r")
#for lines in f:
#    match = re.fullmatch(x,lines.rstrip("\n"))
#    if match is not None:
#        lst.append(lines)
#    else:
#        lst1.append(lines)
#print(lst)
#print(lst1)
                                                   #output
                       #      ['kl09au2345\n', 'kl23er1234\n', 'kl98TM5687\n']
                                    #['kl34e\n', 'jh34rs9023986']