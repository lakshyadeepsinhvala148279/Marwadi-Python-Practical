import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD")
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Marwadi")

mycursor.execute("CREATE TABLE customers (name VARCHAR(255),city VARCHAR(255))")

print("Database created")

mydb.close()
