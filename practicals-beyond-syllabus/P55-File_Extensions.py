# Identify potentially risky file extensions.
# Accept file name
print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

filename = input("Enter file name: ")

# List of potentially risky extensions
extensions = [".exe", ".bat", ".vbs", ".scr", ".cmd"]

# Check file extension
if filename.lower().endswith(tuple(extensions)):
    print("Potentially risky file")
else:
    print("Extension not in the risky list")
