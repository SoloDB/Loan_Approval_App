# save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        ApplicantIncome = float(request.form['ApplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        # gender
        if (gender == "Male"):
            male = 1
        else:
            male = 0

        # married
        if (married == "Yes"):
            married_yes = 1
        else:
            married_yes = 0

        # dependents
        if (dependents == '1'):
            dep = 1
        elif (dependents == '2'):
            dep = 2
        elif (dependents == "3+"):
            dep = 3
        else:
            dep = 0

            # education
        if (education == "Not Graduate"):
            graduate = 0
        else:
            graduate = 1

        # employed
        if (employed == "Yes"):
            employed_yes = 1
        else:
            employed_yes = 0

        prediction = model.predict([[male, married_yes, dep, graduate,
                                     employed_yes, ApplicantIncome, LoanAmount]])
        if prediction == "N":
            prediction_text = "Not Approved"
        else:
            prediction_text = "Approved"
        return render_template("prediction.html", prediction_text)

    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True)
