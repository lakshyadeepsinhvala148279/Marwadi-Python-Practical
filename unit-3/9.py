#Python programs to demonstrate the use of file handling

#create and write data  to a file

file = open("security_log.txt","w")
file.write("cyber security Lab\n")
file.write("Msc Cyber Security and Cyber Law\n")
file.write("File handling is important for manging security law\n")
file.close()

#Read data from the file
file = open("security_log.txt","r")
data = file.read()
print("File Contents:")
print(data)
file.close()

#Append new data to the file
file = open("security_log.txt","a")
file.write("New seurity event recorded\n")
file.close()

#Read the updated file
file = open("security_log.txt","r")
print("Upadate file contents:")
print(file.read())
file.close()
