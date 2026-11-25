print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import matplotlib.pyplot as plt

categories = ["Semester 1", "Semester 2", "Semester 3", "Semester 4"]
students = [45, 50, 48, 52]

plt.bar(categories, students, color="skyblue")
plt.title("Student Count per Semester")
plt.xlabel("Semesters")
plt.ylabel("Number of Students")
plt.show()
print("Bar graph displayed successfully.")
