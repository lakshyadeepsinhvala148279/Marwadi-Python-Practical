import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="Marwadi"
)

mycursor = mydb.cursor()

mycursor.executemany(
    "INSERT INTO customers (name, city) VALUES (%s, %s)",
    [
        ("Amit", "Ahmedabad"),
        ("Priya", "Surat"),
        ("Jay", "Vadodara")
    ]
)

mydb.commit()

print("records inserted successfully.")

mydb.close()

