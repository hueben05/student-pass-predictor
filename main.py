# Student Pass Predictor

# Step 1: Import libraries
import pandas as pd

# Step 2: Create dataset

student_data = [
    [8, 100, 100, 90, 1],
    [3, 50, 62, 70, 0],
    [5, 85, 86, 87, 1]
]

data = pd.DataFrame(student_data, columns=[
    "study_hours",
    "attendance_percent",
    "homework_completion_percent",
    "quiz_average",
    "passed"
])

print(data)

print("Project setup complete.")
