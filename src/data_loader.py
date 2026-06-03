"""
Data Loader Module
Handles loading and basic preparation of the phishing email dataset.
"""

import pandas as pd
import os


def load_dataset(data_path="data/phishing_emails.csv"):
    """
    Load the phishing email dataset from CSV file.
    """
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at: {data_path}")
    
    print("[Data Loader] Loading dataset...")
    df = pd.read_csv(data_path)
    
    # Drop unnecessary column if it exists
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    
    # Standardize column names
    df = df.rename(columns={
        'Email Text': 'email_text',
        'Email Type': 'label'
    })
    
    print(f"[Data Loader] Dataset loaded successfully. Total rows: {len(df)}")
    return df


if __name__ == "__main__":
    # Test the function
    df = load_dataset()
    print(df.head())