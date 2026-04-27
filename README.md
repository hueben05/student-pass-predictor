# Student Pass Predictor

This project uses machine learning to predict whether a student will pass or fail based on study habits and performance.

## Features
- Study hours
- Attendance
- Homework completion
- Quiz scores

## Model
- Logistic Regression (scikit-learn)

## Current Progress
+ Created dataset
+ Structured data using pandas
+ Split data into features (X) and label (y)
+ Performed train/test split
+ Trained a Logistic Regression model
+ Generated predictions and evaluated accuracy
+ Building a Flask web app to allow users to input student data and get predictions in real time

## Results

- The model is able to predict whether a student will pass or fail based on their data  
- It currently gets about **100% accuracy**, but this is on a very small test set  
- This project walks through the full machine learning process: from creating data, to training a model, to making predictions, and checking results  

## Notes

- This is a small, prototype dataset, so the high accuracy isn’t fully reliable yet  
- With more data, the model would give more realistic and consistent results  
- A next step would be expanding the dataset and improving how well the model generalizes to new students

## What I Learned
+ How to structure data for machine learning (features vs labels)
+ How to split data into training and testing sets
+ Why models should not be trained and tested on the same data
+ How to train a Logistic Regression model using scikit-learn
+ How to make predictions on new data and evaluate model accuracy  
+ The importance of having enough data, since small datasets can give misleading results  
