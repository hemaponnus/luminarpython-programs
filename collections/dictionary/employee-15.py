
   # 15/3/21--15

# id ,ename,design, salary(key,value)

#1. name
#2. company
#3. company luminar
#4. salary add 15000
#5. print all key value pairs

#1

employee={"id":1001,"ename":"arun","design":"kollam","salary":1000}
print(employee)
print(employee["ename"])                                               # arun


# 2

print("company"in employee)
                                           # false


#3

employee["company"]="luminar"
#print(employee)         #{'id': 1001, 'name': 'arun', 'design': 'kollam', 'salary': 100, 'company': 'luminar'}


# 4

employee["salary"]+=15000

# 5

for i in employee:
     print(i,"",employee[i])