import mysql.connector
mydb = mysql.connector.connect(host="tiwsal.dz", user="user2022stg01", passwd="Nz2ck99$")
if mydb:
    print('Success')
else:
    print('No success')
