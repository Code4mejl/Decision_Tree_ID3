from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# load model and training columns
model, columns = pickle.load(open("id31_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    outlook = request.form["Outlook"]
    temperature = request.form["Temperature"]
    humidity = request.form["Humidity"]
    wind = request.form["Wind"]

    # create dataframe
    input_data = pd.DataFrame([[outlook, temperature, humidity, wind]],
                              columns=["Outlook","Temperature","Humidity","Wind"])

    # convert to dummies
    input_data = pd.get_dummies(input_data)

    # match training columns
    input_data = input_data.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_data)[0]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)