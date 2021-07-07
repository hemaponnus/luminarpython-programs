

  # 15/3/21--15

pattern="ABCDBCA"
#words=pattern.split(" ")
#print(words)
dic={}
for i in pattern:
    if(i not in dic):
      dic[i]=1
    else:
        print("first reccurssive character",i)
        break

                         # o/p

                 # first reccurssive character   B