##  Phishing Email Detection System

A complete machine learning-powered system that detects phishing emails using Natural Language Processing and additional engineered features. Includes a professional API and an interactive dashboard.

##  Features

- Detects phishing emails with **~96.5% accuracy**
- Uses TF-IDF + smart features (URLs, exclamation marks)
- Professional **FastAPI** backend with detailed responses
- Interactive **Streamlit dashboard** with URL analysis
- Deployed and publicly accessible online

## Live Demo

**API Base URL:** `https://phishing-email-detector-api.onrender.com`  
**Dashboard:** Run locally using the instructions below

##  Tech Stack

- **Python**
- **FastAPI** (Backend API)
- **Streamlit** (Dashboard)
- **Scikit-learn** (Machine Learning)
- **Render** (Deployment)

##  Model Performance

| Model              | Accuracy  |
|--------------------|-----------|
| Logistic Regression| 95.81%    |
| **Random Forest**  | **96.48%** |

**Best Model:** Random Forest

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
├── dashboard.py          # Streamlit Dashboard
├── app.py                # FastAPI Application
├── main.py               # Training script
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
```

## How to Run Locally

### 1. Clone the repository
```
git clone https://github.com/YOUR_USERNAME/phishing-email-detector-api.git
cd phishing-email-detector-api
```
### 2. Create virtual environment & install dependencies
```
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
```
### 3. Run the API
```
uvicorn app:app --reload
```
### 4. Run the Dashboard (in another terminal)
```
streamlit run dashboard.py
```
### API Endpoints
Method,Endpoint,Description
GET,/,API status
GET,/health,Health check
POST,/predict,Predict if email is phishing

### Example Request
```
POST /predict
{
  "email_text": "Your invoice for May 2026 is ready..."
}
```
### Example Response
```
{
  "prediction": "Safe Email",
  "confidence": 78.5,
  "phishing_probability": 21.5,
  "safe_probability": 78.5,
  "timestamp": "2026-06-03T..."
}
```
###Key Highlights

- Clean modular code structure
- Professional API with confidence scores and probability breakdown
- URL analysis feature in dashboard
- Deployed on free hosting (Render)

### Future Improvements

- Add sender reputation & header analysis
- Integrate with real email clients (Gmail/Outlook extension)
- Use advanced models (BERT, transformers)
- Add user authentication for the dashboard

## Built as a Cybersecurity Internship Project


