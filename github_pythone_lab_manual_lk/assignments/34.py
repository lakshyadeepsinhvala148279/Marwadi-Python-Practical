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

cursor.execute("UPDATE Students SET age = 23 WHERE id = 1")
conn.commit()

cursor.execute("SELECT * FROM Students")
rows = cursor.fetchall()

print("Updated Table Records:")
for row in rows:
    print(row)

cursor.close()
conn.close()
