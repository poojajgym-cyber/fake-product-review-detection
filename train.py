import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Dummy dataset (for testing only)
reviews = ["Good product", "Superb quality", "Fake product", "Poor service"]
labels = [1, 1, 0, 0]  # 1 = Genuine, 0 = Fake

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(reviews)

# Train
model = LogisticRegression()
model.fit(X, labels)

# Save
os.makedirs("model", exist_ok=True)
with open("model/fake_review_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("✅ Dummy model trained and saved at model/fake_review_model.pkl")
