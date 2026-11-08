
import pandas as pd

# Load the original dataset
df = pd.read_csv("students.csv")

print("CAMPUSPULSE - DATA CLEANING")
print("=" * 40)

# 1. Display dataset information
print("\nOriginal Dataset Shape:")
print(df.shape)

# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# 4. Check invalid values
print("\nInvalid Values:")

print("Invalid Study Hours:",
      ((df["Study_Hours"] < 0) | (df["Study_Hours"] > 24)).sum())

print("Invalid Attendance:",
      ((df["Attendance"] < 0) | (df["Attendance"] > 100)).sum())

print("Invalid Sleep Hours:",
      ((df["Sleep_Hours"] < 0) | (df["Sleep_Hours"] > 24)).sum())

print("Invalid Final Scores:",
      ((df["Final_Score"] < 0) | (df["Final_Score"] > 100)).sum())

# 5. Remove duplicate records
df = df.drop_duplicates()

# 6. Handle missing values
df = df.dropna()

# 7. Save cleaned dataset
df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned Dataset Shape:")
print(df.shape)

print("\nCleaned dataset saved successfully!")
