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
#sql="create table employee(eid int,ename varchar(25),desig varchar(30),salary int)"
#cursor.execute(sql)
#db.close()
                          ## table created in cmd

#sql="insert into employee(eid,ename,desig,salary)values(101,'vijay','developer',25000)"
#try:
#    cursor.execute(sql)
#    db.commit()
#except Exception as e:
#    print(e.args)
#    db.rollback()
#finally:
#    db.close()
                        ## inserted values



#sql="delete from employee where eid='101'"
#try:
#    cursor.execute(sql)
#    db.commit()
#except Exception as e:
#    print(e.args)
#    db.rollback()
#finally:
#    db.close()
                              ## deleted values from table


#sql="insert into employee(eid,ename,desig,salary)values(101,'vijay','developer',25000)"
#try:
#    cursor.execute(sql)
#    db.commit()
#except Exception as e:
#    print(e.args)
#    db.rollback()
#finally:
#    db.close()
                                    ## value inserted


#sql="update employee set ename='ajay' where eid=102"
#try:
#    cursor.execute(sql)
#    db.commit()
#except Exception as e:
#    print(e.args)
#    db.rollback()
#finally:
#    db.close()
                                ## updated ename


#sql="update employee set eid=100 where ename='ajay'"
#try:
#    cursor.execute(sql)
#    db.commit()
#except Exception as e:
#    print(e.args)
#    db.rollback()
#finally:
#    db.close()
                              ## updated eid

#sql="update employee set salary=26000 where eid=101"
#try:
#    cursor.execute(sql)
#    db.commit()
#except Exception as e:
#    print(e.args)
#    db.rollback()
#finally:
#    db.close()
                            ## updated salary