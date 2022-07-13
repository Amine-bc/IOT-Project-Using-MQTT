import mysql.connector
import json
mydb = mysql.connector.connect(host="tiwsal.dz", user="user2022stg01", passwd="Nz2ck99$")
if mydb:
    print('Success')
else:
    print('No success')
cursor = mydb.cursor()
#cursor.execute("Create database Aminbtest") // Create a database
#cursor.execute("Create table tabletst(name varchar(200), sal int(20))") // Create a table
#cursor.execute("Drop table tabletst")
""" cursor.execute("Show tables")
for tb in cursor:
    print(tb) """
cursor.execute("select * from 03amineb")
result = cursor.fetchall()
for data in result:
    print(data)