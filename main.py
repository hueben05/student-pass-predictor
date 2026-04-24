# Student Pass Predictor

# Step 1: Import libraries
import pandas as pd

# Step 2: Create dataset

student_data = [
    [8, 100, 100, 90, 1],
    [3, 50, 62, 70, 0],
    [5, 85, 86, 87, 1]
]

#Step 3: Convert to DataFrame

data = pd.DataFrame(student_data, columns=[
    "study_hours",
    "attendance_percent",
    "homework_completion_percent",
    "quiz_average",
    "passed"
])

print(data)

#Step 4: Split into features and labels

label_y = data["passed"]
features_X = data.drop("passed", axis = 1)

print("Project setup complete.")
