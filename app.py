# ==========================================
# HDI PREDICTOR - FLASK APP
# ==========================================

from flask import Flask, render_template, request
import numpy as np
import joblib
import os

# ==========================================
# CREATE FLASK APP
# ==========================================

app = Flask(__name__)

# ==========================================
# CHECK MODEL FILES
# ==========================================

required_files = [
    "hdi_model.pkl",
    "scaler.pkl",
    "label_encoder.pkl"
]

for file in required_files:
    if not os.path.exists(file):
        raise FileNotFoundError(
            f"'{file}' not found.\n"
            "Please run Phase 6 to generate the model files."
        )

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("hdi_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

print("✅ Model Loaded Successfully!")

# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")

# ==========================================
# PREDICTION
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get Input Values
        life = float(request.form["life"])
        expected = float(request.form["expected"])
        mean = float(request.form["mean"])
        gni = float(request.form["gni"])

        # Feature Array
        features = np.array([[life, expected, mean, gni]])

        # Scale
        features = scaler.transform(features)

        # Predict
        prediction = model.predict(features)

        # Decode Prediction
        result = label_encoder.inverse_transform(prediction)[0].strip()

        # Colors
        colors = {
            "Very High": "#2ecc71",
            "High": "#3498db",
            "Medium": "#f39c12",
            "Low": "#e74c3c"
        }

        color = colors.get(result, "#3498db")

        # Recommendations
        recommendations = {

            "Very High": [
                "Maintain high-quality healthcare services.",
                "Continue investing in higher education and research.",
                "Promote sustainable economic growth.",
                "Strengthen digital infrastructure."
            ],

            "High": [
                "Improve healthcare infrastructure.",
                "Increase access to higher education.",
                "Create more employment opportunities.",
                "Reduce regional inequalities."
            ],

            "Medium": [
                "Increase literacy and school enrollment.",
                "Improve healthcare accessibility.",
                "Invest in infrastructure development.",
                "Support skill development programs."
            ],

            "Low": [
                "Improve basic healthcare facilities.",
                "Increase school enrollment.",
                "Reduce poverty through employment.",
                "Improve sanitation and clean drinking water."
            ]

        }

        print("Prediction:", result)
        print("Recommendations:", recommendations.get(result))

        return render_template(
            "index.html",
            prediction=result,
            color=color,
            recommendations=recommendations.get(result, [])
        )

    except Exception as e:

        print(e)

        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}",
            color="#e74c3c",
            recommendations=[]
        )

# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )