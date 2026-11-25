
#r+ - Read and write mode
file = open("security_log.txt","r+")
print("r+ mode:")
print(file.read())
file.write("Additional data using r+ mode.\n")
file.close()

# w+ - Write and Read mode
file = open("security_report.txt", "w+")
file.write("Security Report\n")
file.write("Threat analysis completed.\n")
file.seek(0)
print("w+ Mode:")
print(file.read())
file.close()


# a+ - Append and Read mode
file = open("security_report.txt", "a+")
file.write("Security report updated.\n")
file.seek(0)
print("a+ Mode:")
print(file.read())
file.close()
