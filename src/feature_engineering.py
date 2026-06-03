from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from scipy.sparse import hstack
import numpy as np

def create_features(df, text_column='cleaned_text', max_features=5000):
    print("[Feature Engineering] Creating TF-IDF + extra features...")
    
    vectorizer = TfidfVectorizer(max_features=max_features, stop_words='english')
    X_text = vectorizer.fit_transform(df[text_column])
    
    # Add extra numerical features
    extra_features = df[['url_count', 'exclamation_count', 'urgent_word_count']].values
    X = hstack([X_text, extra_features])
    
    y = df['label']
    
    print(f"[Feature Engineering] Feature shape: {X.shape}")
    return X, y, vectorizer


def split_data(X, y, test_size=0.2, random_state=42):
    print("[Feature Engineering] Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    print(f"Training samples: {X_train.shape[0]}, Testing samples: {X_test.shape[0]}")
    return X_train, X_test, y_train, y_test