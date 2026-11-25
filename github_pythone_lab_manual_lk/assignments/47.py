print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import re

text = "For queries contact test.user@gmail.com or admin@domain.co.in."
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("Detected Email Addresses:")
for email in emails:
    print(email)
