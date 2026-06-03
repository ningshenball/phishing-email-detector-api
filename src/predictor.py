"""
Predictor Module
Handles loading the saved model and making predictions on new emails.
"""

import joblib
import os

# Smart import that works in both cases
try:
    from .text_cleaner import clean_text
except ImportError:
    from text_cleaner import clean_text


def load_model_and_vectorizer(model_path="models/best_phishing_model.pkl", 
                               vectorizer_path="models/vectorizer.pkl"):
    """
    Load the trained model and vectorizer from disk.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at: {model_path}")
    if not os.path.exists(vectorizer_path):
        raise FileNotFoundError(f"Vectorizer not found at: {vectorizer_path}")

    print("[Predictor] Loading saved model and vectorizer...")
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    print("[Predictor] Model and vectorizer loaded successfully.")
    return model, vectorizer


def predict_single_email(email_text, model, vectorizer):
    """
    Predict whether a single email is Phishing or Safe.
    Returns: (prediction, confidence in %)
    """
    cleaned_text = clean_text(email_text)
    vectorized = vectorizer.transform([cleaned_text])
    
    prediction = model.predict(vectorized)[0]
    probability = model.predict_proba(vectorized)[0]
    
    if prediction == "Phishing Email":
        confidence = probability[1]
    else:
        confidence = probability[0]
    
    return prediction, round(confidence * 100, 2)


if __name__ == "__main__":
    print("Predictor module loaded successfully.")