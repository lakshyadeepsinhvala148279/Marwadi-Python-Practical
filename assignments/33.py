import os
print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="python"
)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Students (id INT PRIMARY KEY, name VARCHAR(50), age INT)")

cursor.execute("INSERT INTO Students VALUES (1, 'Alice', 22)")
cursor.execute("INSERT INTO Students VALUES (2, 'Bob', 24)")
conn.commit()

cursor.execute("SELECT * FROM Students")
rows = cursor.fetchall()

print("Table Records:")
for row in rows:
    print(row)

cursor.close()
conn.close()
