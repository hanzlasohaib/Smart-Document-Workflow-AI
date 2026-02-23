import joblib
import os

# Load model once at startup
MODEL_PATH = os.path.join(os.getcwd(), "document_classifier.pkl")
model = joblib.load(MODEL_PATH)


def classify_text(text: str):
    prediction = model.predict([text])[0]
    probabilities = model.predict_proba([text])[0]
    confidence = max(probabilities)

    return prediction, float(confidence)
