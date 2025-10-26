import pandas as pd
import random

platforms = ["YouTube", "Coursera", "Udemy", "FreeCodeCamp", "SoloLearn", "Others"]
languages = ["Python", "JavaScript", "C++", "Java", "HTML/CSS", "SQL"]
challenges = [
    "Lack of time",
    "Difficult concepts",
    "Poor internet connection",
    "Lack of motivation",
    "Limited resources",
    "No mentor support"
]

data = {
    "Age": [random.randint(16, 35) for _ in range(50)],
    "Hours of coding per week": [random.randint(2, 25) for _ in range(50)],
    "Platform used most": [random.choice(platforms) for _ in range(50)],
    "Programming language": [random.choice(languages) for _ in range(50)],
    "Progress rating (1–5)": [random.randint(1, 5) for _ in range(50)],
    "Main challenge faced": [random.choice(challenges) for _ in range(50)]
}

df = pd.DataFrame(data)
df.to_csv("survey_data.csv", index=False)

print("✅ survey_data.csv created successfully!")
