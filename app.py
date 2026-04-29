from flask import Flask, render_template, request
from main import model

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Get input values from form
    study_hours = int(request.form["study_hours"])
    attendance = int(request.form["attendance"])
    homework = int(request.form["homework"])
    quiz = int(request.form["quiz"])

    # Prepare data for model
    input_data = [[study_hours, attendance, homework, quiz]]

    # Make prediction
    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)

    # Convert prediction to readable result
    if prediction[0] == 1:
        confidence = (probabilities[0][1]) * 100
        result = f"Pass {confidence:.2f}%"
    else:
        confidence = (probabilities[0][0]) * 100
        result = f"Fail {confidence:.2f}%"

    return render_template("index.html", result=result)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
