
import pandas as pd
import matplotlib.pyplot as plt

# Sample academic dataset
data = {
    "Student": ["Aarav", "Priya", "Rahul", "Neha", "Kabir",
                "Ananya", "Rohan", "Isha"],
    "Maths": [85, 92, 67, 78, 88, 95, 72, 90],
    "Science": [88, 95, 70, 82, 84, 91, 75, 93],
    "English": [79, 89, 74, 85, 81, 94, 78, 87]
}

df = pd.DataFrame(data)

# Calculate performance metrics
subjects = ["Maths", "Science", "English"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

# Sort students by average marks
df = df.sort_values("Average", ascending=False)

print("=" * 45)
print("     STUDENT PERFORMANCE ANALYSIS")
print("=" * 45)

print("\nStudent Performance:")
print(df.to_string(index=False, formatters={
    "Average": "{:.2f}".format
}))

print("\nSubject-wise Average Marks:")
print(df[subjects].mean().round(2))

print("\nTop Performer:")
topper = df.iloc[0]
print(f"{topper['Student']} — {topper['Average']:.2f}% average")

print("\nClass Average:")
print(f"{df['Average'].mean():.2f}%")

# Save analysis results
df.to_csv("student_performance_results.csv", index=False)

# Create a chart
plt.figure(figsize=(9, 5))
plt.bar(df["Student"], df["Average"])
plt.title("Student Average Marks")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("student_performance_chart.png")
plt.close()

print("\nResults saved to CSV and chart files.")
