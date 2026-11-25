print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import matplotlib.pyplot as plt

scores = [55, 62, 67, 70, 72, 75, 78, 81, 85, 88, 90, 95]

plt.hist(scores, bins=5, edgecolor="black")
plt.title("Score Distribution")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()
print("Histogram displayed successfully.")
