#Import the regular expression module
import re
#1.searching the pattern
# ------------------------------------
text = "Cybersecurity Lab 2026"
# Check if the text contains any number
if re.search(r'\d', text):
    print("1. The string contains a number.")
else:
    print("1. No number found in the string.")

# ------------------------------------
# 2. Extracting Emails
# ------------------------------------
text_with_emails = "Contact us at support@cyberlab.com or admin@cyberlab.com"
# Pattern to find valid email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text_with_emails)
print("2. Extracted Emails:", emails)

# ------------------------------------
# 3. Validating a Phone Number
# ------------------------------------
phone = "9876543210"
# Pattern for 10-digit phone number
if re.fullmatch(r'\d{10}', phone):
    print("3. Valid phone number.")
else:
    print("3. Invalid phone number.")


# ------------------------------------
# 4. Finding Capitalized Words
# ------------------------------------
sentence = "Python Is Fun And Important"
# Find all words starting with capital letters
capital_words = re.findall(r'\b[A-Z][a-z]*\b', sentence)
print("4. Words starting with capital letters:", capital_words)

# ------------------------------------
# 5. Replacing Digits
# ------------------------------------
text_with_digits = "Server123 has IP456"
# Replace all digits with '#'
replaced_text = re.sub(r'\d', '#', text_with_digits)
print("5. Text after replacing digits:", replaced_text)
