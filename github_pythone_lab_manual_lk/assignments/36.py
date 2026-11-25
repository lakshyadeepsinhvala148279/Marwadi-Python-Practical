print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [22, 24, 23],
    "City": ["New York", "London", "Paris"],
}

df = pd.DataFrame(data)
print("DataFrame Output:")
print(df)
