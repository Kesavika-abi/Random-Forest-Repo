from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        age = int(request.form["age"])
        job_satisfaction = int(request.form["job_satisfaction"])
        monthly_income = float(request.form["monthly_income"])
        years_at_company = int(request.form["years_at_company"])
        work_life_balance = int(request.form["work_life_balance"])
        overtime = request.form["overtime"]

        # Encode overtime manually (Yes=1, No=0)
        overtime_encoded = 1 if overtime.lower() == "yes" else 0

        features = np.array([[age, job_satisfaction, monthly_income, years_at_company, work_life_balance, overtime_encoded]])
        prediction = model.predict(features)[0]

        # Prediction message
        result = "Yes - Employee will leave" if prediction == 1 else "No - Employee will stay"

        return render_template("result.html", result=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
