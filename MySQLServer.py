import getpass
import mysql.connector
from mysql.connector import Error

# Connect to MySQL server
try:
    password = getpass.getpass("Enter your MySQL password: ")

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=password
    )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully")

except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")