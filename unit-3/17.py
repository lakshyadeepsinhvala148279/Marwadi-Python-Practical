print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

try:
    x = 10
    y = 2
    print("Result:", x / y)
except ZeroDivisionError:
    print("Error occurred!")
finally:
    print("Execution completed. Cleanup operations can be performed here.")
