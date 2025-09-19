import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# -----------------------------
# Step 1: Expanded Training Dataset
# -----------------------------
reviews = [
    # Genuine reviews
    "Good product", "Superb quality", "Excellent service", "Value for money",
    "Highly recommended", "Very satisfied", "Amazing experience",
    "Product is worth buying", "Great quality and fast delivery",
    "Really happy with this purchase",

    # Fake reviews
    "Fake product", "Worst item ever", "Poor service", "Total waste of money",
    "Not worth buying", "Terrible quality", "Completely useless",
    "Bad experience", "Worst purchase ever", "Totally waste of money"
]

labels = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,   # Genuine = 1
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0    # Fake = 0
]

# Lowercase all reviews for consistency
reviews = [r.lower() for r in reviews]

# -----------------------------
# Step 2: Vectorize Text
# -----------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(reviews)

# -----------------------------
# Step 3: Train Model
# -----------------------------
model = LogisticRegression()
model.fit(X, labels)

# -----------------------------
# Step 4: Save Model + Vectorizer
# -----------------------------
os.makedirs("model", exist_ok=True)

with open("model/fake_review_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("✅ Model trained and saved at: model/fake_review_model.pkl")
