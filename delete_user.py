import mysql.connector
from mysql.connector import Error
import connectionfile

my_db = connectionfile.create_connections()
mycursor =my_db.cursor()

USE_DB= "USE abc_school  "
mycursor.execute(USE_DB)

sql = "DELETE FROM class_12 WHERE FIRST_NAME = 'JAY' AND LAST_NAME = 'MULEVA'"
mycursor.execute(sql)

my_db.commit()

print(mycursor.rowcount, "record(s) deleted")