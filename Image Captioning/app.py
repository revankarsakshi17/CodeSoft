import os
import sys
from flask import Flask, render_template, request, jsonify
from deepface import DeepFace
import numpy as np
from PIL import Image

# Fix Windows terminal Unicode printing
sys.stdout.reconfigure(encoding="utf-8")

# Disable slow TensorFlow optimizations
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

app = Flask(__name__)

# ---------------------- CAPTION GENERATION ----------------------

def generate_caption(mood):
    captions = {
        "happy": "This picture captures a joyful and cheerful moment.",
        "sad": "This image reflects a quiet or emotional moment.",
        "angry": "This expression shows frustration or anger.",
        "surprise": "This moment looks surprising or unexpected!",
        "fear": "This face expresses fear or uncertainty.",
        "neutral": "A calm and neutral expression.",
        "disgust": "This face shows distaste or disgust.",
        "contempt": "This expression displays contempt or disdain.",
    }
    return captions.get(mood.lower(), f"Detected a strong feeling: {mood}")

# ---------------------- ROUTES ----------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        file = request.files["image"]
        img_path = os.path.join("static", "uploaded.jpg")
        file.save(img_path)

        # DeepFace expects file path for stable detection
        result = DeepFace.analyze(
            img_path=img_path,
            actions=["emotion"],
            enforce_detection=False
        )

        # Handle DeepFace response format
        if isinstance(result, list):
            dominant = result[0]["dominant_emotion"]
        else:
            dominant = result["dominant_emotion"]

        caption = generate_caption(dominant)

        return jsonify({"mood": dominant, "caption": caption})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

#.venv\Scripts\Activate.ps1
