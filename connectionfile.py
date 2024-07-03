import mysql.connector


def create_connections():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql@123"
    )
    return mydb


def commit():
    return None


def cursor():
    return None