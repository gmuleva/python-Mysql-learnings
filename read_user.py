import mysql.connector
from mysql.connector import Error
import connectionfile

my_db = connectionfile.create_connections()
mycursor =my_db.cursor(buffered=True) #why we uses buffered = true?answer it google it

USE_DB= "USE abc_school"
mycursor.execute(USE_DB)

sql = "SELECT FIRST_NAME FROM class_12"
mycursor.execute(sql)

a=my_db.commit()
print(a)

