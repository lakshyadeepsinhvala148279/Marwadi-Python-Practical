print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

try:
    a = 20
    b = 5
    res = a / b
except ZeroDivisionError:
    print("Error: Division by zero occurred.")
else:
    print(f"Division successful! Result: {res}")
