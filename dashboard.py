import streamlit as st
import requests
import re
from datetime import datetime

st.set_page_config(page_title="Phishing Email Detector", page_icon="🛡️", layout="centered")

st.title("🛡️ Phishing Email Detector")
st.markdown("Paste any email content below to check if it's **phishing** or **safe**.")

st.warning("⚠️ This tool is for educational and internal use only. Results may not be 100% accurate.")

email_text = st.text_area("Paste Email Content Here:", height=220)

API_URL = "https://phishing-email-detector-api.onrender.com/predict"

def extract_urls(text):
    return re.findall(r'https?://[^\s]+|www\.[^\s]+', text)

def analyze_urls(urls):
    suspicious = []
    for url in urls:
        url_lower = url.lower()
        if any(x in url_lower for x in ['bit.ly', 'tinyurl', 'goo.gl', 't.co', 'short.link']):
            suspicious.append(f"Shortened URL detected: {url}")
        if re.search(r'\d+\.\d+\.\d+\.\d+', url):
            suspicious.append(f"IP address in URL: {url}")
        if len(url) > 100:
            suspicious.append(f"Very long/suspicious URL: {url[:80]}...")
    return suspicious

if st.button("🔍 Analyze Email", use_container_width=True):
    if not email_text.strip():
        st.error("Please paste some email content.")
    else:
        with st.spinner("Analyzing..."):
            try:
                # Get model prediction
                response = requests.post(API_URL, json={"email_text": email_text})
                result = response.json()

                # URL Analysis
                urls = extract_urls(email_text)
                suspicious_urls = analyze_urls(urls)

                # Final Decision Logic
                model_says_phishing = result["prediction"] == "Phishing Email"
                high_confidence = result["confidence"] >= 75
                has_suspicious_url = len(suspicious_urls) > 0

                final_risk = "Safe"
                risk_color = "green"

                if model_says_phishing and (high_confidence or has_suspicious_url):
                    final_risk = "High Risk - Phishing"
                    risk_color = "red"
                elif model_says_phishing or has_suspicious_url:
                    final_risk = "Possible Phishing"
                    risk_color = "orange"

                # Display Results
                if final_risk == "High Risk - Phishing":
                    st.error(f"🚨 **{final_risk}** (Model Confidence: {result['confidence']}%)")
                elif final_risk == "Possible Phishing":
                    st.warning(f"⚠️ **{final_risk}** (Model Confidence: {result['confidence']}%)")
                else:
                    st.success(f"✅ **{final_risk}** (Model Confidence: {result['confidence']}%)")

                # Show details
                st.subheader("Analysis Breakdown")
                st.write(f"**Model Prediction**: {result['prediction']}")
                st.write(f"**Phishing Probability**: {result['phishing_probability']}%")
                st.write(f"**Safe Probability**: {result['safe_probability']}%")

                if urls:
                    st.write(f"**URLs Found**: {len(urls)}")
                    if suspicious_urls:
                        st.error("**Suspicious URLs Detected:**")
                        for s in suspicious_urls:
                            st.write(f"- {s}")
                    else:
                        st.success("No obviously suspicious URLs found.")
                else:
                    st.info("No URLs found in the email.")

                st.caption(f"Checked at: {result['timestamp']}")

            except Exception as e:
                st.error(f"Error: {e}")