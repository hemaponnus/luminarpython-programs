# mysql-connector (package installed)

   # step 1 :-   import mysql module

import mysql.connector

    # step 2 :-   establish connection

           # mysql -u root -p Password@123 (in ubandu) (connect in mysql shell:connectionestablish)
db=mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password"

)

    # step 3 :-   create curser object ( transport data )
          # in insert quary we are giving datas to mysql

cursor=db.cursor()

    # step 4 :- execute sql queries

sql="select version()"
cursor.execute(sql)
#data=cursor.fetchone()
#print(data)

    # step 5 :- close connection

db.close()