
  # 15/3/21--15

#line="hai hello hai hello hai"

#hai,3
#hello,2

# split                                       # o/p
#print(line)                          #    hai hello hai hello hai
#hai
# hello
# hai
# hello
# hai

#words=line.split(" ")                         # o/p
#print(words)                        # ['hai', 'hello', 'hai', 'hello', 'hai']

#['hai', 'hello', 'hai', 'hello', 'hai']

# key     # value
# hai        1 +1 +1 +1
#hello       1  +1 +1 +1

#for i in words:
#      print(i)
#dic={}

#print("hai" in words)


## program

line="hai hello hai hello hai"
word=line.split(" ")
print(word)
#['hai', 'hello', 'hai', 'hello', 'hai']
dic={}
for i in word:         #hai
    if(i not in dic):  # hai
        dic[i]=1       # dic[hello]=1
    else:                                                  # o/p
        dic[i]+=1
print(dic)                                         #   {'hai': 3, 'hello': 2}



# key     # value
# hai        1 +1 +1 +1
#hello       1  +1 +1 +1