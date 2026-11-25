import pandas as pd
data = {
    'Name': ['pari', 'esha', 'nisha', 'ridhhi'],
    'Age': [21, 20, 21, 19],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Chennai']
}

df = pd.DataFrame(data)

print(df)
print(df.loc[1])
