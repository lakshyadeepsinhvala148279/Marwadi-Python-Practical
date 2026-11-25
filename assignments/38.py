print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "JavaScript"]
shares = [40, 25, 15, 20]

plt.pie(shares, labels=languages, autopct="%1.1f%%")
plt.title("Programming Language Popularity")
plt.show()
print("Pie chart displayed successfully.")
