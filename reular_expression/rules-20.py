# 23/3/21-20
 # rules

#1  #x = "[abc]"                               ## either a,b,c
#2  #x = "[^abc]"                              ## except a,b,c
#3  #x = "[a-z]"                               ## check a-z
#4  #x = "[A-Z]"                               ## check A-Z
#5  #x = "[a-zA-z]"                            ## check a-z,A-Z
#6  #x = "[0-9]"                               ## check numbers
#7  #x = "[^a-zA-z0-9]"                        ## check symbols
#8  #x = "\s"                                  ## check space
#9  #x = "\d                                   ## check digits
#10 #x = "\D                                   ## except digits
#11 #x = "\w"                                  ## check words except special charecters
#12 #x = "\W"                                  ## special charecters
#13 #x ="[^a-zA-Z0-9]"                         ## "  "

        ## quantifiers

#1 #x="a+"                ## a including group
#2 #x="a*"                ## count including zero no of a (group)
#3 #x="a?"                ## count including zero no of a (individual)
#4 #x="a{3}"              ## count  only 3a
#5 #x="a{1,3}"            ## count min 1,max 3 a
#6 #x="^a"                ## count if stating with a
#7 #x="a$"                ## count if ending with a
