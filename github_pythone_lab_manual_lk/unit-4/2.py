import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="Marwadi"
)

mycursor = mydb.cursor()
mycursor.execute("""
    CREATE TABLE customers (
        name VARCHAR(255),
        city VARCHAR(255)
    )
""")

print("Table created successfully")

mydb.close()
