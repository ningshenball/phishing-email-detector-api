# Phishing Email Detection API

A machine learning-powered API that detects whether an email is **Phishing** or **Safe** using Natural Language Processing and additional engineered features.

## 🚀 Features

- Detects phishing emails with high accuracy (~96.4%)
- Uses TF-IDF + extra features (URLs, exclamation marks, urgent words)
- Built with **FastAPI** for fast and clean API responses
- Deployed and publicly accessible

## 🛠 Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas & NumPy
- Render (Deployment)

## 📊 Model Performance

| Model              | Accuracy |
|--------------------|----------|
| Logistic Regression| 95.60%   |
| Random Forest      | **96.38%** |

**Best Model:** Random Forest

## 🔗 Live API

**Base URL:** `https://phishing-email-detector-api.onrender.com`

### Endpoints

| Method | Endpoint     | Description                  |
|--------|--------------|------------------------------|
| GET    | `/`          | API status                   |
| GET    | `/health`    | Health check                 |
| POST   | `/predict`   | Predict if email is phishing |

### Example Request

```json
POST /predict
{
  "email_text": "Congratulations! You have won a free iPhone. Click here to claim now."
}
```
## Example Response
```
{
  "prediction": "Phishing Email",
  "confidence": 97,
  "phishing_probability": 97,
  "safe_probability": 3,
  "timestamp": "2026-06-03T12:34:22.986534"
}
```

## Project Structure
```
phishing_email_detector/
├── src/
│   ├── data_loader.py
│   ├── text_cleaner.py
│   ├── feature_engineering.py
│   ├── model_trainer.py
│   └── predictor.py
├── models/
│   ├── best_phishing_model.pkl
│   └── vectorizer.pkl
├── app.py
├── main.py
├── test_api.py
├── requirements.txt
├── Procfile
└── README.md
```
## How to Run Locally
```
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the API
uvicorn app:app --reload
# Then open: http://127.0.0.1:8000/docs
```
## Future Improvements
- Add URL analysis and header features
- Build a simple frontend
- Add user authentication
- Improve model with deep learning (BERT)

## Built as part of a Cybersecurity Internship project
