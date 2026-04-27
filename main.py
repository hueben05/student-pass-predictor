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

# Step 5: Train/test split
X_train, X_test, y_train, y_test = train_test_split(features_X, label_y, test_size=0.33, random_state=42)

# Step 6: Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 7: Make predictions
predictions = model.predict(X_test)

# Step 8: Evaluate model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, predictions)

print("Predictions:", predictions)
print("Actual:", y_test.values)
print("Accuracy:", accuracy)
