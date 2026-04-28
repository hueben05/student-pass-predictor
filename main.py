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
    [3, 80, 60, 55, 0]
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
