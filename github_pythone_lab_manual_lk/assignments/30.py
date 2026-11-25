print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

with open("demo.txt", "w") as f:
    f.write("Line 1: Writing mode ('w')\n")

with open("demo.txt", "a") as f:
    f.write("Line 2: Appending mode ('a')\n")

with open("demo.txt", "r") as f:
    print(f.read())
    
