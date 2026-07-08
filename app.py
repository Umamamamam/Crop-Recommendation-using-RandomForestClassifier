"""
app.py
Simple Flask backend that loads the trained model (model.pkl)
and exposes:
  - "/"          -> serves the website (index.html)
  - "/predict"   -> receives form data (N, P, K, temperature, humidity, ph, rainfall)
                    and returns the predicted crop as JSON

Run with:
    python app.py
Then open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model once when the server starts
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Collect the 7 inputs in the correct order
        values = [float(data[feature]) for feature in FEATURES]
        input_array = np.array(values).reshape(1, -1)

        # Predict the crop
        prediction = model.predict(input_array)[0]

        # Also get the top 3 most likely crops with probabilities
        probabilities = model.predict_proba(input_array)[0]
        classes = model.classes_
        top3_idx = np.argsort(probabilities)[::-1][:3]
        top3 = [
            {"crop": classes[i], "confidence": round(float(probabilities[i]) * 100, 2)}
            for i in top3_idx
        ]

        return jsonify({
            "success": True,
            "prediction": prediction,
            "top3": top3
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
