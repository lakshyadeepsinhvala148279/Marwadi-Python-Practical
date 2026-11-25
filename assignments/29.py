print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

file = open("sample.txt", "w")
file.write("Hello, World!\nWelcome to File Handling in Python.")
file.close()

file = open("sample.txt", "r")
content = file.read()
print("File Contents:\n" + content)
file.close()
