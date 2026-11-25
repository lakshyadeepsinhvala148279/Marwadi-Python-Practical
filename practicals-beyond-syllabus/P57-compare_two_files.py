print("M.sc. (CS&CL) Semester 1")
print("Enrollment No: [ENROLLMENT NUMBER]")

try:
    with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
        data1 = file1.read()
        data2 = file2.read()

    if data1 == data2:
        print("Both files are identical")
    else:
        print("Files are different")

except FileNotFoundError:
    print("Error: One or both files were not found.")
