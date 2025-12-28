from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

app = Flask(__name__)

#Load trained model
with open(MODEL_PATH, "rb") as f:
    model =  pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction =  None

    if request.method == "POST":
        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        prev_score = float(request.form["prev_score"])

        #Create Dataframe with correct feature names
        input_data=pd.DataFrame(
            [[hours, attendance, prev_score]],
            columns=["hours_studied", "attendance", "previous_score"]
        )

        raw_prediction = model.predict(input_data)[0]
        prediction = round(min(max(raw_prediction, 0), 100), 2)

    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run()