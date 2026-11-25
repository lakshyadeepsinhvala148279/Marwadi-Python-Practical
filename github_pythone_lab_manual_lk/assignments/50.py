print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import os

path = "."
files = os.listdir(path)

print(f"Files and Directory Contents in '{os.path.abspath(path)}':")
for file in files:
    print(file)
