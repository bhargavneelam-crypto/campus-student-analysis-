
import pandas as pd
import numpy as np

# Generate sample student data
np.random.seed(42)

total_students = 500

data = {
    "Student_ID": [f"S{i:03d}" for i in range(1, total_students + 1)],
    "Study_Hours": np.random.uniform(1, 10, total_students).round(1),
    "Attendance": np.random.randint(50, 101, total_students),
    "Sleep_Hours": np.random.uniform(4, 10, total_students).round(1),
    "Assignment_Score": np.random.randint(40, 101, total_students),
    "Previous_Score": np.random.randint(40, 101, total_students)
}

df = pd.DataFrame(data)
df["Final_Score"] = (
    0.35 * df["Study_Hours"] * 10 +
    0.20 * df["Attendance"] +
    0.15 * df["Assignment_Score"] +
    0.20 * df["Previous_Score"] +
    0.10 * df["Sleep_Hours"] * 10
).round(1)
df["Final_Score"] = df["Final_Score"].clip(0, 100)
df.to_csv("students.csv", index=False)

print("CampusPulse Dataset Created Successfully!")
print("\nFirst 5 Student Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)
