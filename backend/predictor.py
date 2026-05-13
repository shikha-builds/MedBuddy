import os
import logging
from pathlib import Path

import pandas as pd
from joblib import load

PROJECT_ROOT = Path(__file__).resolve().parent  # backend folder

MODEL_PATH = PROJECT_ROOT / "model_dir" / "heart_disease_prediction_model.joblib"
LOG_PATH = PROJECT_ROOT / "logs" / "app.log"

LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_PATH)
    ]
)
 
# load model
model = load(MODEL_PATH)
logging.info("Model loaded successfully.")

# prediction function
def predict(input_data: dict):

    df = pd.DataFrame([input_data])

    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])

    logging.info(
        f"Prediction: {prediction}, Probability: {probability}"
    )

    return {
        "prediction": prediction,
        "probability": probability
    }