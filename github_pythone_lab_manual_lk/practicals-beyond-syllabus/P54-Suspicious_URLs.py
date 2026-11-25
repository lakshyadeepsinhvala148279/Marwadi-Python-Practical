# Identify suspicious keywords in a URL.
# Accept URL from the user
print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

url = input("Enter a URL: ")

# List of suspicious keywords
words = ["login", "verify", "bank", "free", "password"]

# Convert URL into lowercase
url = url.lower()

# Check suspicious keywords
found = False

for word in words:
    if word in url:
        print("Suspicious keyword found:", word)
        found = True

if found:
    print("Warning: URL needs further inspection")
else:
    print("No listed suspicious keywords found")
