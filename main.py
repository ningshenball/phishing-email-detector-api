from src.data_loader import load_dataset
from src.text_cleaner import clean_dataframe
from src.feature_engineering import create_features, split_data
from src.model_trainer import train_and_select_best_model
import joblib
import os

print("\n" + "=" * 65)
print("          PHISHING EMAIL DETECTION MODEL (Improved v2)")
print("          Cybersecurity Intern Project")
print("=" * 65)

print("\n[Step 1] Loading and cleaning data...")
df = load_dataset()
df = clean_dataframe(df)

print("\n[Step 2] Creating TF-IDF features...")
X, y, vectorizer = create_features(df)

X_train, X_test, y_train, y_test = split_data(X, y)

print("\n[Step 3] Training and comparing models...")
best_model, best_name, best_acc = train_and_select_best_model(
    X_train, X_test, y_train, y_test
)

print("\n[Step 4] Saving best model...")
os.makedirs("models", exist_ok=True)
joblib.dump(best_model, "models/best_phishing_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print(f"\nBest model saved: {best_name} ({best_acc:.2%} accuracy)")
print("\n" + "=" * 65)
print("Training completed successfully!")
print("=" * 65 + "\n")