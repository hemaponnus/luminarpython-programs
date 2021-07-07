
  #12/3/21--14


      ## tuples
    ################                                           ## properties
                                                        ###########################

 #1. how to define?
                           # parathesis
#tp=()
#print(type(tp))
#tp1=tuple()
#print(type(tp1))

#tp=(10,10.5,"hema",True,True)                           # support hetrogenious data
#print(tp)                                               # support duplicates values
tp=(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8)
print(tp)                                                # it preserves insertion value
tp(1)=100                                                # immutable
print(tp)
