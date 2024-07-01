import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql@123"
    )
    mycursor = mydb.cursor()

    # mycursor.execute("CREATE DATABASE Abc_school")
    # print("Database is created successfully")

    mycursor.execute("USE Abc_school")
    '''mycursor.execute("""
        CREATE TABLE CLASS_12 (
            FIRST_NAME VARCHAR(255),
            LAST_NAME VARCHAR(255),
            DOB DATE,
            EMAIL VARCHAR(255),
            PHONE_NUMBER VARCHAR(20)
        );
    """)
    print("Table CLASS_12 is created successfully")'''

    mycursor.execute("""
    INSERT INTO CLASS_12 (FIRST_NAME, LAST_NAME, DOB, EMAIL, PHONE_NUMBER) 
    VALUES 
    ('GOURAV', 'MULEVA', '2003-10-05', 'gouravmuleva635@gmail.com', '6265799745'),
    ('JAY', 'MULEVA', '2001-07-26', 'JAYMULEVA@gmail.com', '6265649753'),
    ('AADITYA', 'MULEVA', '2000-09-09', 'AADITYA@gmail.com', '7045876976'),
    ('ARPITA', 'MULEVA', '2001-03-20', 'arpita67@gmail.com', '9993056645'),
    ('KRISHNA', 'RATHOD', '2009-07-04', 'krishu@gmail.com', '8799875634');
    """)
    mydb.commit()
    print("Records inserted successfully")

except Error as e:
    print(f"Error: {e}")

finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()