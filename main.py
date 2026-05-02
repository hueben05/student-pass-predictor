import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dataset
student_data = [
    [8, 100, 100, 90, 1],
    [3, 50, 62, 70, 0],
    [5, 85, 86, 87, 1],
    [7, 95, 98, 88, 1],
    [2, 51, 33, 65, 0],
    [6, 75, 82, 80, 1],
    [9, 96, 88, 68, 1],
    [1, 80, 78, 100, 0],
    [1, 30, 50, 50, 0],
    [0, 40, 30, 45, 0],
    [2, 60, 55, 58, 0],
    [4, 70, 65, 60, 0],
    [3, 80, 60, 55, 0],
    [8, 65, 85, 80, 1],
    [3, 100, 75, 80, 1],
    [1, 90, 65, 50, 0],
    [4, 55, 95, 80, 1],
    [6, 78, 100, 60, 0],
    [4, 68, 72, 70, 0],
    [5, 70, 75, 72, 1],
    [3, 85, 70, 68, 0],
    [6, 65, 78, 74, 1],
    [4, 90, 60, 66, 0],
    [5, 88, 65, 70, 1],
    [2, 95, 85, 62, 0],
    [7, 60, 70, 75, 1],
    [3, 75, 80, 69, 0],
    [4, 78, 82, 71, 1],
    [5, 62, 90, 68, 0],
    [6, 68, 88, 72, 1],
    [2, 82, 60, 74, 0],
    [5, 80, 70, 65, 0],
    [6, 85, 72, 67, 1],
    [4, 72, 68, 76, 0],
    [5, 74, 70, 78, 1],
    [3, 88, 75, 64, 0],
    [6, 73, 76, 70, 1],
    [4, 66, 85, 73, 0],
    [5, 69, 88, 75, 1],
    [2, 76, 92, 70, 0],
    [7, 64, 65, 80, 1],
    [3, 70, 90, 66, 0],
    [4, 82, 73, 69, 1],
    [5, 77, 67, 71, 0],
    [6, 79, 69, 73, 1],
    [4, 60, 100, 78, 1],
    [3, 92, 55, 72, 0],
    [5, 83, 80, 68, 1],
    [2, 89, 78, 75, 0],
    [6, 71, 74, 69, 1]
]

# Convert to DataFrame
data = pd.DataFrame(student_data, columns=[
    "study_hours",
    "attendance_percent",
    "homework_completion_percent",
    "quiz_average",
    "passed"
])

# Split into features and label
features_X = data.drop("passed", axis=1)
label_y = data["passed"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    features_X, label_y, test_size=0.33, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model (only runs when main.py is executed directly)
if __name__ == "__main__":
    predictions = model.predict(X_test)

    print("Predictions:", predictions)
    print("Actual:", y_test.values)

    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy:", accuracy)
