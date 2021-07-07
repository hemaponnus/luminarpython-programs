import mysql.connector

    # step 2 :-   establish connection

db=mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="Password@123",
    database="mydb",
    auth_plugin="mysql_native_password"
)

    # step 3 :-   create curser object ( transport data )

cursor=db.cursor()
f=open("C:/Users/hemaponnus/PycharmProjects/feb python/collections/pythontomysql/employee")
for lines in f:
    data=lines.rstrip("\n").split(",")
    sql="insert into employee(eid,ename,desig,salary)values(%s,%S,%s,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()
db.close()