from src.data_loader import load_dataset
from src.text_cleaner import clean_dataframe
from src.feature_engineering import create_features, split_data
from src.model_trainer import train_and_select_best_model
import joblib
import os
import numpy as np
from scipy.sparse import hstack

print("\n" + "=" * 65)
print("          PHISHING EMAIL DETECTION MODEL (Improved)")
print("          Cybersecurity Intern Project")
print("=" * 65)

# Step 1: Load and clean data + extract extra features
print("\n[Step 1] Loading and cleaning data with extra features...")
df = load_dataset()
df = clean_dataframe(df)

# Step 2: Create features (TF-IDF + extra features)
print("\n[Step 2] Creating TF-IDF + extra features...")
X, y, vectorizer = create_features(df)

# Step 3: Split data
X_train, X_test, y_train, y_test = split_data(X, y)

# Step 4: Train and select best model
print("\n[Step 3] Training and comparing models...")
best_model, best_name, best_acc = train_and_select_best_model(
    X_train, X_test, y_train, y_test
)

# Step 5: Save model and vectorizer
print("\n[Step 4] Saving best model...")
os.makedirs("models", exist_ok=True)
joblib.dump(best_model, "models/best_phishing_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
print(f"Best model saved: {best_name} ({best_acc:.2%} accuracy)")

print("\n" + "=" * 65)
print("Training completed successfully!")
print("=" * 65 + "\n")