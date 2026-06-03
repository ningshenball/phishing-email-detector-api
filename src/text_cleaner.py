import re
import string
import pandas as pd

def clean_text(text):
    if pd.isna(text):
        return "", 0, 0
    
    text = str(text).lower()
    
    # Only keep useful simple features
    url_count = len(re.findall(r'http\S+|www\S+', text))
    exclamation_count = text.count('!')
    
    # Clean text
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text, url_count, exclamation_count


def clean_dataframe(df, text_column='email_text'):
    print("[Text Cleaner] Cleaning text and extracting features...")
    
    results = df[text_column].apply(clean_text)
    
    df['cleaned_text'] = results.apply(lambda x: x[0])
    df['url_count'] = results.apply(lambda x: x[1])
    df['exclamation_count'] = results.apply(lambda x: x[2])
    
    df = df[df['cleaned_text'].str.len() > 0]
    
    print(f"[Text Cleaner] Done. Final rows: {len(df)}")
    return df