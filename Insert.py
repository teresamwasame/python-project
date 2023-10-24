import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE,ADDRESS,SALARY)\
             VALUES(11,'EMOBILIS',7,'WESTLANDS',25000.00)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE,ADDRESS,SALARY)\
             VALUES(12,'SAFARICOM',9,'WESTLANDS',25000.00)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE,ADDRESS,SALARY)\
             VALUES(13,'MICROSOFT',2,'WESTLANDS',25000.00)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE,ADDRESS,SALARY)\
             VALUES(14,'ORACLE',5,'WESTLANDS',25000.00)");


conn.commit()
print("Records created successfuly")
conn.close()