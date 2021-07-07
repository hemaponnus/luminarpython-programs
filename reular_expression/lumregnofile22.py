import re
f2=open("validing","a")
x="([L][U][M]\d{2}[P][Y]\d{3}$)"
f=open("lumregno","r")
for lines in f:
    data=lines.rstrip("\n")
    matcher=re.fullmatch(x,data)
    if matcher is not None:
        f2.write(data)
        f2.write("\n")
                                      ## output

                             # file: validing


#import re
#x="(\w{3}\d{2}[P][Y]\d{3})"
#f=open("lumregno","r")
#for lines in f:
#    data=lines.rstrip("\n")
#    matcher=re.fullmatch(x,data)
#    if matcher is not None:
#        print(data,"valid")
                                                    #output
                             # LUM12PY678  valid
                             # LUM12PY676  valid
                             # LUM11Py679  valid
#import re
#lst=[]
#lst1=[]
#x="(\w{3}\d{2}[P][Y]\d{3}$)"
#f=open("lumregno","r")
#for lines in f:
#    data=lines.rstrip("\n")
#    matcher=re.fullmatch(x,data)
#    if matcher is not None:
#        lst.append(data)
#    else:
#        lst1.append(data)
#print(lst)
#print(lst1)
                                          # output
                      #['LUM12PY678', 'LUM12PY676', 'LUM11PY679']
                      #['LUM13BD609', 'LUM12DS678', 'LUM13DS609', 'LUM19BD601', 'LUM10BD601']