from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from datetime import datetime
from src.text_cleaner import clean_text
import numpy as np
from scipy.sparse import hstack

# ====================== Load Model ======================
print("[API] Loading model and vectorizer...")
model = joblib.load("models/best_phishing_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")
print("[API] Model loaded successfully.")

# ====================== FastAPI App ======================
app = FastAPI(
    title="Phishing Email Detection API",
    description="A professional API to detect phishing emails using Machine Learning",
    version="1.1"
)

class EmailRequest(BaseModel):
    email_text: str

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    phishing_probability: float
    safe_probability: float
    timestamp: str

# ====================== Endpoints ======================

@app.get("/")
def home():
    return {
        "message": "Phishing Email Detection API is running",
        "version": "1.1"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True,
        "timestamp": datetime.now().isoformat()
    }

@app.post("/predict", response_model=PredictionResponse)
def predict_email(request: EmailRequest):
    cleaned_text, url_count, exclamation_count, urgent_word_count = clean_text(request.email_text)
    vectorized_text = vectorizer.transform([cleaned_text])
    
    extra = np.array([[url_count, exclamation_count, urgent_word_count]])
    final_vector = hstack([vectorized_text, extra])
    
    prediction = model.predict(final_vector)[0]
    probabilities = model.predict_proba(final_vector)[0]
    
    classes = model.classes_
    proba_dict = dict(zip(classes, probabilities))
    
    phishing_prob = proba_dict.get("Phishing Email", 0)
    safe_prob = proba_dict.get("Safe Email", 0)
    
    if prediction == "Phishing Email":
        confidence = phishing_prob
    else:
        confidence = safe_prob
    
    return {
        "prediction": prediction,
        "confidence": round(confidence * 100, 2),
        "phishing_probability": round(phishing_prob * 100, 2),
        "safe_probability": round(safe_prob * 100, 2),
        "timestamp": datetime.now().isoformat()
    }