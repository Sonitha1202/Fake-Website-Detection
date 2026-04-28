"""
AI Project: Phishing Website Detection System

Project Description:
This project uses Artificial Intelligence and Machine Learning
to detect whether a website link is SAFE or PHISHING (fake).

Why this project is strong:
- Very unique and practical AI project
- Cybersecurity + AI combination
- Strong value for placements and interviews
- Looks advanced on GitHub
- Easy to explain in viva

Technologies Used:
- Python
- Scikit-learn
- CountVectorizer
- Naive Bayes Classifier

How to Run:
1. Install Python
2. Install required library:
   pip install scikit-learn
3. Run the file:
   python phishing_website_detection.py
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

print("=== AI Phishing Website Detection System ===\n")

# Sample website links
website_links = [
    "https://www.amazon.com",
    "https://www.google.com",
    "https://www.microsoft.com",
    "https://www.github.com",
    "http://free-money-login-now.xyz",
    "http://bank-verification-alert.ru",
    "http://claim-prize-fast.win",
    "http://secure-account-update.fake"
]

# Labels: 1 = Safe Website, 0 = Phishing Website
labels = [1, 1, 1, 1, 0, 0, 0, 0]

# Convert links into numerical form
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(website_links)

# Train model
model = MultinomialNB()
model.fit(X, labels)

print("This system checks whether a website link is SAFE or PHISHING.\n")
print("Example: https://www.amazon.com\n")

user_input = input("Enter website link: ")

user_vector = vectorizer.transform([user_input])
prediction = model.predict(user_vector)

print("\nDetection Result:")

if prediction[0] == 1:
    print("This looks like a SAFE Website")
else:
    print("This looks like a PHISHING / FAKE Website")
