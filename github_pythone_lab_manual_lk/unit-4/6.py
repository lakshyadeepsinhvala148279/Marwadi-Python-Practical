import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="Marwadi"
)

mycursor = mydb.cursor()

# 7. DELETE DATABASE / TABLE
sql = "DROP DATABASE marwadi"
mycursor.execute(sql)

print("Database deleted")

# 8. CLOSE CONNECTION
mycursor.close()
mydb.close()
