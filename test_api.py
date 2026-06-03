import requests

url = "http://127.0.0.1:8000/predict"

# Test emails
test_emails = [
    "Congratulations! You have won a free iPhone. Click here to claim now.",
    "Hey, just checking if we're still meeting for lunch tomorrow?",
    "Urgent: Your bank account has been compromised. Verify immediately or lose access."
]

print("Testing Phishing Detection API...\n")

for i, email in enumerate(test_emails, 1):
    payload = {"email_text": email}
    
    try:
        response = requests.post(url, json=payload)
        result = response.json()
        
        print(f"Test {i}:")
        print(f"Email     : {email[:70]}...")
        print(f"Prediction: {result['prediction']}")
        print(f"Confidence: {result['confidence']}%\n")
        
    except Exception as e:
        print(f"Error: {e}\n")