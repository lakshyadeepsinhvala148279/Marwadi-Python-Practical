import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="Marwadi"
)

mycursor = mydb.cursor()

# 5. FETCH & DISPLAY DATA
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

print(myresult)
print("\nCustomers in the table:")

for row in myresult:
    print(row)

mydb.close()
