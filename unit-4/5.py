import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="Marwadi"
)

mycursor = mydb.cursor()

# 6. UPDATE TABLE DATA
sql = "UPDATE customers SET city='Rajkot' WHERE city='Ahmedabad'"
mycursor.execute(sql)

# Note: Your connection variable is named 'mydb', not 'conn'
mydb.commit()

print(mycursor.rowcount, "record affected")

mydb.close()
