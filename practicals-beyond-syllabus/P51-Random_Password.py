#Write a Python program to generate a random password.

# Import random module
print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import random

# Define characters for password
characters = "abcdefghijk123456789@#$"

# Create an empty password
password = ""

# Generate 8 characters
for i in range(8):
    password = password + random.choice(characters)

# Display password
print("Generated Password:", password)
