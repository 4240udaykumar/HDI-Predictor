# ==========================================
# HDI PREDICTOR - FLASK WEB APPLICATION
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
# PROJECT DIRECTORY
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==========================================
# MODEL FILE PATHS
# ==========================================

MODEL_PATH = os.path.join(BASE_DIR, "hdi_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "label_encoder.pkl")

# ==========================================
# CHECK REQUIRED FILES
# ==========================================

required_files = [
    MODEL_PATH,
    SCALER_PATH,
    ENCODER_PATH
]

for file in required_files:

    if not os.path.exists(file):

        raise FileNotFoundError(
            f"\nRequired file not found:\n{file}\n\n"
            "Please run the training script (Phase 6) to generate the model files."
        )

# ==========================================
# LOAD MODEL FILES
# ==========================================

print("Loading Model...")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
label_encoder = joblib.load(ENCODER_PATH)

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

        # -----------------------------
        # Read User Inputs
        # -----------------------------

        life = float(request.form["life"])
        expected = float(request.form["expected"])
        mean = float(request.form["mean"])
        gni = float(request.form["gni"])

        # -----------------------------
        # Create Input Array
        # -----------------------------

        sample = np.array([
            [
                life,
                expected,
                mean,
                gni
            ]
        ])

        # -----------------------------
        # Scale Features
        # -----------------------------

        sample = scaler.transform(sample)

        # -----------------------------
        # Predict
        # -----------------------------

        prediction = model.predict(sample)

        result = label_encoder.inverse_transform(prediction)[0]

        # -----------------------------
        # Prediction Colors
        # -----------------------------

        colors = {
            "Very High": "#2ecc71",
            "High": "#3498db",
            "Medium": "#f39c12",
            "Low": "#e74c3c"
        }

        color = colors.get(result, "#3498db")

        # -----------------------------
        # Return Result
        # -----------------------------

        return render_template(
            "index.html",
            prediction=result,
            color=color
        )

    except ValueError:

        return render_template(
            "index.html",
            prediction="Please enter valid numeric values.",
            color="#e74c3c"
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}",
            color="#e74c3c"
        )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)