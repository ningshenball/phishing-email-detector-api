"""
Model Trainer Module
Trains multiple models and selects the best one.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_logistic_regression(X_train, y_train):
    """Train Logistic Regression model."""
    print("[Model Trainer] Training Logistic Regression...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model


def train_random_forest(X_train, y_train):
    """Train Random Forest model."""
    print("[Model Trainer] Training Random Forest...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, model_name):
    """Evaluate model and return accuracy."""
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"[Model Trainer] {model_name} Accuracy: {accuracy:.4f}")
    return accuracy


def train_and_select_best_model(X_train, X_test, y_train, y_test):
    """
    Train both models, compare accuracy, and return the best one.
    """
    print("\n[Model Trainer] Starting model training and comparison...")
    
    # Train both models
    lr_model = train_logistic_regression(X_train, y_train)
    rf_model = train_random_forest(X_train, y_train)
    
    # Evaluate both
    lr_acc = evaluate_model(lr_model, X_test, y_test, "Logistic Regression")
    rf_acc = evaluate_model(rf_model, X_test, y_test, "Random Forest")
    
    # Select best model
    if rf_acc > lr_acc:
        best_model = rf_model
        best_name = "Random Forest"
        best_acc = rf_acc
    else:
        best_model = lr_model
        best_name = "Logistic Regression"
        best_acc = lr_acc
    
    print(f"\n[Model Trainer] Best Model: {best_name} ({best_acc:.4f})")
    
    return best_model, best_name, best_acc


if __name__ == "__main__":
    print("Model Trainer module loaded successfully.")