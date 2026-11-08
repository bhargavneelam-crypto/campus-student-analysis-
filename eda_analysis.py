
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_students.csv")

print("=" * 50)
print("       CAMPUSPULSE - EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# 1. Basic statistics
print("\n1. BASIC STATISTICS")
print(df.describe().round(2))

# 2. Average calculations
print("\n2. STUDENT AVERAGES")

print("Average Study Hours:",
      round(df["Study_Hours"].mean(), 2))

print("Average Attendance:",
      round(df["Attendance"].mean(), 2))

print("Average Sleep Hours:",
      round(df["Sleep_Hours"].mean(), 2))

print("Average Final Score:",
      round(df["Final_Score"].mean(), 2))

# 3. Highest and lowest scores
print("\n3. PERFORMANCE ANALYSIS")

top_student = df.loc[df["Final_Score"].idxmax()]
low_student = df.loc[df["Final_Score"].idxmin()]

print("Highest Scoring Student:")
print(top_student)

print("\nLowest Scoring Student:")
print(low_student)

# 4. Performance categories
def performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Average"
    else:
        return "Needs Improvement"

df["Performance"] = df["Final_Score"].apply(performance)

print("\n4. PERFORMANCE DISTRIBUTION")
print(df["Performance"].value_counts())

# 5. Correlation analysis
print("\n5. CORRELATION ANALYSIS")

correlation = df[
    ["Study_Hours", "Attendance", "Sleep_Hours",
     "Assignment_Score", "Previous_Score", "Final_Score"]
].corr()

print(correlation.round(2))

# 6. Save analysis results
df.to_csv("analysis_results.csv", index=False)

print("\nEDA COMPLETED SUCCESSFULLY!")
