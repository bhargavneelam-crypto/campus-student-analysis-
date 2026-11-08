
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load analysed dataset
df = pd.read_csv("analysis_results.csv")

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Set chart style
sns.set_theme(style="whitegrid")

# 1. Final Score Distribution
plt.figure(figsize=(9, 5))

sns.histplot(df["Final_Score"], bins=20, kde=True)

plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")

plt.savefig("charts/score_distribution.png")
plt.show()


# 2. Study Hours vs Final Score
plt.figure(figsize=(9, 5))

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Final_Score",
    hue="Performance"
)

plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")

plt.savefig("charts/study_vs_score.png")
plt.show()


# 3. Performance Distribution
plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Performance",
    order=["Excellent", "Good", "Average", "Needs Improvement"]
)

plt.title("Student Performance Distribution")
plt.xlabel("Performance Category")
plt.ylabel("Number of Students")
plt.xticks(rotation=15)

plt.savefig("charts/performance_distribution.png")
plt.show()


# 4. Attendance vs Final Score
plt.figure(figsize=(9, 5))

sns.regplot(
    data=df,
    x="Attendance",
    y="Final_Score",
    scatter_kws={"alpha": 0.5}
)

plt.title("Attendance vs Final Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")

plt.savefig("charts/attendance_vs_score.png")
plt.show()


# 5. Correlation Heatmap
plt.figure(figsize=(10, 7))

correlation = df[
    ["Study_Hours", "Attendance", "Sleep_Hours",
     "Assignment_Score", "Previous_Score", "Final_Score"]
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Student Data Correlation Heatmap")

plt.savefig("charts/correlation_heatmap.png")
plt.show()


print("All CampusPulse charts created successfully!")
