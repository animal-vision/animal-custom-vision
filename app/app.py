import os
import requests
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
from .main.routes import main # Remove the dot at the beginning of .main.routes to main.routes for local deployment hosting

# Load API keys from .env file
load_dotenv()
AZURE_URL = os.getenv("AZURE_URL")
PREDICTION_KEY = os.getenv("PREDICTION_KEY")

app = Flask(__name__)
UPLOAD_FOLDER = "app/static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.register_blueprint(main)

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Handle image upload & API call
@app.route("/analyse", methods=["POST"])
def analyse():
    if "image" not in request.files:
        return render_template("index.html", error="No image uploaded.")

    image = request.files["image"]
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    if image.filename == "":
        return render_template("index.html", error="No file selected.")

    if not allowed_file(image.filename):
        return render_template("index.html", error="Unsupported file type. Please upload a PNG, JPG, or GIF.")

    # Save image to static/uploads folder
    image_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
    image.save(image_path)

    headers = {
        "Prediction-Key": PREDICTION_KEY,
        "Content-Type": "application/octet-stream"
    }

    with open(image_path, "rb") as img:
        response = requests.post(AZURE_URL, headers=headers, data=img.read())

    if response.status_code != 200:
        return f"Error: {response.text}", response.status_code

    predictions = response.json().get("predictions", [])

    # Filter out tags with low confidence scores
    THRESHOLD = 50
    filtered_predictions = [
        p for p in predictions if p["probability"] * 100 >= THRESHOLD
    ]

    # Remove duplicates & keep only highest probability for each tag
    unique_predictions = {}
    for p in filtered_predictions:
        tag = p["tagName"]
        probability = p["probability"]

        if tag not in unique_predictions or probability > unique_predictions[tag]["probability"]:
            unique_predictions[tag] = {
                "tagName": tag,
                "probability": probability
            }

    # Change dictionary back to a list
    final_predictions = list(unique_predictions.values())

    # Add colour coding based on confidence levels
    for p in final_predictions:
        if p["probability"] > 0.8:
            p["color"] = "green"
        elif p["probability"] > 0.5:
            p["color"] = "orange"
        else:
            p["color"] = "red"

    no_tags_found = len(final_predictions) == 0

    return render_template(
        "results.html",
        predictions=final_predictions,
        image_url=url_for("static", filename=f"uploads/{image.filename}"),
        no_tags_found=no_tags_found
    )

if __name__ == "__main__":
    app.run(debug=True)
