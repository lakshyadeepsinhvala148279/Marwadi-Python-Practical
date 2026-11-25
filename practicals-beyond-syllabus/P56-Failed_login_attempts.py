# Read a sample security log and count failed login attempts.
# Open the sample log file
print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

file = open("login.txt", "r")

# Initialize counter
count = 0

# Read each line
for line in file:
    if "Failed" in line:
        count = count + 1

# Display result
print("Failed login attempts:", count)

# Close file
file.close()
