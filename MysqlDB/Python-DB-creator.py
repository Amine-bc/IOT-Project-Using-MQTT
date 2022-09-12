import mysql.connector
import json
mydb = mysql.connector.connect(host="#####", user="#####", passwd="#####",database="#####")
cursor = mydb.cursor()
#cursor.execute("Create database Aminbtest") // Create a database
#cursor.execute("Create table tst(topic varchar(100), data int(10))") #// Create a table
cursor.execute("Drop table tst") #// Delete a table
""" cursor.execute("Show tables")
for tb in cursor:
    print(tb) """
#Here print the table
#cursor.execute("select * from 03amineb")
#result = cursor.fetchall()
#for data in result:
#print(data)
