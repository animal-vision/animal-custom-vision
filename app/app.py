import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from main.routes import main # remove the dot before 'main' before running the website
from azure.storage.blob import BlobServiceClient
from datetime import datetime
from urllib.parse import urlparse

# Load API keys from .env
load_dotenv()
AZURE_URL = os.getenv("AZURE_URL")
PREDICTION_KEY = os.getenv("PREDICTION_KEY")
AZURE_BLOB_CONN = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_CONTAINER = os.getenv("AZURE_STORAGE_CONTAINER")

app = Flask(__name__)
UPLOAD_FOLDER = "app/static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.register_blueprint(main)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Upload to Azure Blob
def upload_to_blob(image):
    blob_service = BlobServiceClient.from_connection_string(AZURE_BLOB_CONN)
    container_client = blob_service.get_container_client(AZURE_CONTAINER)

    blob_name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{image.filename}"
    container_client.upload_blob(blob_name, image, overwrite=True)

    return f"https://{blob_service.account_name}.blob.core.windows.net/{AZURE_CONTAINER}/{blob_name}"

# Home
@app.route("/")
def home():
    return render_template("index.html")

# Upload History
@app.route("/history")
def history():
    try:
        blob_service = BlobServiceClient.from_connection_string(AZURE_BLOB_CONN)
        container_client = blob_service.get_container_client(AZURE_CONTAINER)

        blob_urls = []
        for blob in container_client.list_blobs():
            blob_url = f"https://{blob_service.account_name}.blob.core.windows.net/{AZURE_CONTAINER}/{blob.name}"
            blob_urls.append(blob_url)

        return render_template("history.html", images=blob_urls)

    except Exception as e:
        return render_template("history.html", error=f"Error loading history: {str(e)}")

# Delete Image
@app.route("/delete", methods=["POST"])
def delete_image():
    image_url = request.form.get("image_url")
    if not image_url:
        return redirect("/history")

    try:
        parsed_url = urlparse(image_url)
        blob_name = parsed_url.path.split("/")[-1]

        blob_service = BlobServiceClient.from_connection_string(AZURE_BLOB_CONN)
        container_client = blob_service.get_container_client(AZURE_CONTAINER)
        container_client.delete_blob(blob_name)
    except Exception as e:
        return render_template("history.html", error=f"Failed to delete image: {str(e)}")

    return redirect("/history")

# Analyse Route
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

    # Upload to Azure Blob
    try:
        blob_url = upload_to_blob(image)
    except Exception as e:
        return render_template("index.html", error=f"Azure upload failed: {str(e)}")

    # Rewind file for prediction
    image.stream.seek(0)

    headers = {
        "Prediction-Key": PREDICTION_KEY,
        "Content-Type": "application/octet-stream"
    }

    response = requests.post(AZURE_URL, headers=headers, data=image.read())

    if response.status_code != 200:
        return f"Error: {response.text}", response.status_code

    predictions = response.json().get("predictions", [])

    descriptions = {
        "excessive sleep": "Potential issues include fatigue, depression, or physical discomfort.",
        "skin condition": "Possible conditions include allergies, dermatitis, or fungal infections.",
        "eye condition": "Potential issues may involve conjunctivitis, cataracts, or eye infections.",
        "scratching": "Possible causes include fleas, dermatitis, or fungal infections.",
        "limping": "Potential problems could be related to joint issues, fractures, soft tissue injuries, or arthritis.",
        "back condition": "Possible concerns include arthritis, spinal issues, or muscular strain that affects mobility.",
    }

    THRESHOLD = 50
    filtered_predictions = [p for p in predictions if p["probability"] * 100 >= THRESHOLD]

    unique_predictions = {}
    for p in filtered_predictions:
        tag = p["tagName"]
        prob = p["probability"]
        if tag not in unique_predictions or prob > unique_predictions[tag]["probability"]:
            unique_predictions[tag] = {"tagName": tag, "probability": prob}

    final_predictions = list(unique_predictions.values())

    for p in final_predictions:
        p["color"] = (
            "green" if p["probability"] > 0.8 else
            "orange" if p["probability"] > 0.5 else
            "red"
        )

    no_tags_found = len(final_predictions) == 0

    for p in final_predictions:
        p["description"] = descriptions.get(p["tagName"].lower(), "No additional information available.")

    return render_template(
        "results.html",
        predictions=final_predictions,
        image_url=blob_url,
        no_tags_found=no_tags_found
    )

if __name__ == "__main__":
    app.run(debug=True)
