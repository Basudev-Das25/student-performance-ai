from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

#Load trained model
with open("model.pkl", "rb") as f:
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

        prediction = round(model.predict(input_data)[0], 2)

    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)