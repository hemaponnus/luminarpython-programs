#f=open("data","r")
#dic={}
#for lines in f:
#    words=lines.rstrip("\n ").split(" ")
#    for i in words:
#        if(i not in dic):
#            dic[i]=1
#        else:
#            dic[i]+=1
#print(dic)

                              ## output

#{'I': 4, 'am': 2, 'BHARATH': 1, 'CHANDRAN.': 1, 'M,': 1, 'Employee': 1, 'code': 1, 'â€“': 1, 'IFBAPPL06306': 1, 'working': 2, 'as': 1, 'CSR': 1, 'in': 1, 'Kerala': 1, 'Branch': 1, 'for': 3, 'last': 2, 'few': 1, 'years.': 1, 'leaving': 1, 'my': 7, 'current': 1, 'job': 1, 'to': 3, 'attend': 1, 'next': 1, 'assignment.': 1, 'want': 1, 'state': 1, 'that': 1, 'day': 1, 'with': 1, 'IFB': 1, 'Appliances': 1, 'Ltd.': 1, 'will': 1, 'be': 1, '31/01/2021': 1, 'It': 1, 'was': 1, 'nice': 1, 'and': 5, 'learning': 1, 'phase': 1, 'of': 1, 'professional': 1, 'life.': 1, 'thank': 1, 'all': 1, 'seniors': 1, 'colleagues': 1, 'their': 1, 'guidance': 1, 'supports.': 1, 'Request': 1, 'you': 1, 'process': 1, 'full': 1, 'final': 1, 'settlement,': 1, 'if': 1, 'any,': 1, 'at': 1, 'the': 1, 'earliest': 1, 'issue': 1, 'an': 1, 'experience': 1, 'service': 1, 'letter': 1, 'future': 1, 'endeavour.': 1, '': 1}


                                ## or###

f=open("data","r")
dic={}
for lines in f:
    words=lines.rstrip("\n ").split(" ")
    print(words)
    for i in words:
        if(i not in dic):
            dic[i]=1
        else:
            dic[i]+=1
print(dic)

                     ## output##
#['I', 'am', 'BHARATH', 'CHANDRAN.', 'M,', 'Employee', 'code', 'â€“', 'IFBAPPL06306', 'working', 'as', 'CSR', 'in', 'Kerala', 'Branch', 'for', 'last', 'few', 'years.']
#['I', 'am', 'leaving', 'my', 'current', 'job', 'to', 'attend', 'my', 'next', 'assignment.', 'I', 'want', 'to', 'state', 'that', 'my', 'last', 'working', 'day', 'with', 'IFB', 'Appliances', 'Ltd.', 'will', 'be', '31/01/2021']
#['It', 'was', 'nice', 'and', 'learning', 'phase', 'of', 'my', 'professional', 'life.', 'I', 'thank', 'all', 'my', 'seniors', 'and', 'colleagues', 'for', 'their', 'guidance', 'and', 'supports.']
#['Request', 'you', 'to', 'process', 'my', 'full', 'and', 'final', 'settlement,', 'if', 'any,', 'at', 'the', 'earliest', 'and', 'issue', 'an', 'experience', 'service', 'letter', 'for', 'my', 'future', 'endeavour.']
#['']
#{'I': 4, 'am': 2, 'BHARATH': 1, 'CHANDRAN.': 1, 'M,': 1, 'Employee': 1, 'code': 1, 'â€“': 1, 'IFBAPPL06306': 1, 'working': 2, 'as': 1, 'CSR': 1, 'in': 1, 'Kerala': 1, 'Branch': 1, 'for': 3, 'last': 2, 'few': 1, 'years.': 1, 'leaving': 1, 'my': 7, 'current': 1, 'job': 1, 'to': 3, 'attend': 1, 'next': 1, 'assignment.': 1, 'want': 1, 'state': 1, 'that': 1, 'day': 1, 'with': 1, 'IFB': 1, 'Appliances': 1, 'Ltd.': 1, 'will': 1, 'be': 1, '31/01/2021': 1, 'It': 1, 'was': 1, 'nice': 1, 'and': 5, 'learning': 1, 'phase': 1, 'of': 1, 'professional': 1, 'life.': 1, 'thank': 1, 'all': 1, 'seniors': 1, 'colleagues': 1, 'their': 1, 'guidance': 1, 'supports.': 1, 'Request': 1, 'you': 1, 'process': 1, 'full': 1, 'final': 1, 'settlement,': 1, 'if': 1, 'any,': 1, 'at': 1, 'the': 1, 'earliest': 1, 'issue': 1, 'an': 1, 'experience': 1, 'service': 1, 'letter': 1, 'future': 1, 'endeavour.': 1, '': 1}

