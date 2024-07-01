import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql@123",

    )
    mycursor = mydb.cursor()

    mycursor.execute("use abc_school")
    mycursor.execute("UPDATE class_12 SET LAST_NAME = 'MULEVA' WHERE LAST_NAME = 'RATHOD';")

    mydb.commit()
    print("Records updated successfully")

except Error as e:
    print(f"Error: {e}")

