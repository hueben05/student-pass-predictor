# Student Pass Predictor

This project uses machine learning to predict whether a student will pass or fail based on study habits and performance.

## Features
- Study hours
- Attendance
- Homework completion
- Quiz scores

## Model
- Logistic Regression (scikit-learn)

## Web App
- Users can input study hours, attendance, homework, and quiz scores  
- The Flask app sends this data to the trained model  
- The model returns a pass/fail prediction displayed on the same page
  
## Current Progress
+ Created dataset
+ Structured data using pandas
+ Split data into features (X) and label (y)
+ Performed train/test split
+ Trained a Logistic Regression model
+ Generated predictions and evaluated accuracy
+ Built a Flask web app that allows users to input student data and get predictions in real time

## Results

- The model is able to predict whether a student will pass or fail based on their data  
- It currently gets about **100% accuracy**, but this is on a very small test set  
- This project walks through the full machine learning process: from creating data, to training a model, to making predictions, and checking results
- The app also displays the model’s confidence percentage alongside each prediction
- The app uses color to make results easier to read, showing pass in green and fail in red    

## Notes

- This is a small, prototype dataset, so the high accuracy isn’t fully reliable yet
- The dataset has been expanded with additional edge cases and mixed-performance examples to improve model behavior
- With more data, the model would give more realistic and consistent results  
- A next step would be expanding the dataset and improving how well the model generalizes to new students

## What I Learned
- How to structure data for machine learning (features vs labels)
- How to split data into training and testing sets
- Why models should not be trained and tested on the same data
- How to train a Logistic Regression model using scikit-learn
- How to make predictions on new data and evaluate model accuracy  
- The importance of having enough data, since small datasets can give misleading results
- How to use prediction probabilities to show how confident the model is in its output
- How to use simple conditions in HTML to change how results look based on what the model predicts

## How to Run

1. Install required libraries:

```bash
pip install -r requirements.txt
```

2. Run the Flask app:

```bash
python app.py
```

3. Open your browser and go to:

```text
http://127.0.0.1:5000
```
