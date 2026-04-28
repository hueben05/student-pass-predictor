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

    # Convert prediction to readable result
    result = "Pass" if prediction[0] == 1 else "Fail"

    return render_template("index.html", result=result)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
