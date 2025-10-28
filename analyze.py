import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("survey_data.csv")
print("✅ Data loaded successfully!\n")
print(df.head())  # Show first few rows

# 1️⃣ Most popular programming languages
plt.figure(figsize=(8, 5))
df["Programming language"].value_counts().plot(kind="bar")
plt.title("Most Popular Programming Languages Among Students")
plt.xlabel("Programming Language")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("popular_language.png")
plt.show()

# 2️⃣ Average progress rating per platform
avg_progress = df.groupby("Platform used most")["Progress rating (1–5)"].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
avg_progress.plot(kind="bar", color="skyblue")
plt.title("Average Progress Rating by Learning Platform")
plt.xlabel("Platform")
plt.ylabel("Average Progress Rating")
plt.tight_layout()
plt.savefig("avg_progress_platform.png")
plt.show()

# 3️⃣ Average coding hours by programming language
avg_hours = df.groupby("Programming language")["Hours of coding per week"].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
avg_hours.plot(kind="bar", color="orange")
plt.title("Average Coding Hours by Programming Language")
plt.xlabel("Programming Language")
plt.ylabel("Average Hours per Week")
plt.tight_layout()
plt.savefig("avg_hours_language.png")
plt.show()

# 4️⃣ Most common learning challenges
plt.figure(figsize=(9, 5))
df["Main challenge faced"].value_counts().plot(kind="bar", color="salmon")
plt.title("Most Common Challenges Faced by Coding Students")
plt.xlabel("Challenge")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("commom_challenges.png")
plt.show()

