from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "AgriGuard AI Backend is Working!"
    })


@app.route("/health")
def health():
    return jsonify({
        "success": True,
        "status": "online",
        "message": "Backend Connected Successfully!"
    })


@app.route("/analyze", methods=["POST"])
def analyze():

    image = request.files.get("image")

    if image is None:
        return jsonify({
            "success": False,
            "message": "Please upload or capture an image"
        }), 400

    # Demo AI result
    result = {
        "success": True,

        "crop_disease": {
            "crop": "Tomato",
            "disease": "Tomato Early Blight",
            "confidence": 94.5,
            "severity": "Moderate",
            "description": "Early Blight detected in the tomato leaf.",
            "recommendation": "Remove affected leaves and monitor the crop."
        },

        "satellite": {
            "success": True,
            "satellite": "Sentinel-2",
            "ndvi": 0.65,
            "field_condition": "Healthy"
        }
    }

    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
