print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:[ENROLLMENT NUMBER]")

import pandas as pd

list_data = [["Amit", 85], ["Neha", 90]]
df_list = pd.DataFrame(list_data, columns=["Name", "Marks"])
print("1. From List of Lists:")
print(df_list)

dict_data = {"Subject": ["Python", "DBMS"], "Credits": [4, 3]}
df_dict = pd.DataFrame(dict_data)
print("\n2. From Dictionary:")
print(df_dict)
