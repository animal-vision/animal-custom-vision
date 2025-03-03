import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
AZURE_URL = os.getenv("AZURE_URL")
PREDICTION_KEY = os.getenv("PREDICTION_KEY")

app = Flask(__name__)

# Homepage - upload image
@app.route("/")
def home():
    return render_template("index.html")

# Handle image upload & API call
@app.route("/analyse", methods=["POST"])
def analyse():
    if "image" not in request.files:
        return "No image uploaded", 400

    image = request.files["image"]
    headers = {
        "Prediction-Key": PREDICTION_KEY,
        "Content-Type": "application/octet-stream"
    }
    response = requests.post(AZURE_URL, headers=headers, data=image.read())

    if response.status_code != 200:
        return f"Error: {response.text}", response.status_code

    predictions = response.json().get("predictions", [])

    # Add colour coding based on confidence levels
    for p in predictions:
        if p["probability"] > 0.8:
            p["color"] = "green"
        elif p["probability"] > 0.5:
            p["color"] = "yellow"
        else:
            p["color"] = "red"

    return render_template("results.html", predictions=predictions)

if __name__ == "__main__":
    app.run(debug=True)